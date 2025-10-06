import gzip
import xml.etree.ElementTree as ET
from typing import Dict, Any, Iterator, List


def pubmed_papers_it(file_path: str) -> Iterator[Dict[str, Any]]:
    try:
        # Parse the gzipped XML file
        with gzip.open(file_path) as f:
            tree = ET.parse(f)
            root = tree.getroot()

        # Find all PubmedArticle elements
        for article in root.findall('.//PubmedArticle'):
            article_data = extract_article_data(article)
            if article_data:
                yield article_data

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")


def extract_article_data(article_element) -> Dict[str, Any]:
    article_data = {}

    # Extract article title
    title_elem = article_element.find('.//ArticleTitle')
    if title_elem is not None:
        article_data['title'] = title_elem.text.strip() if title_elem.text else ''
    else:
        article_data['title'] = ''

    # Extract authors
    authors = extract_authors(article_element)
    article_data['authors'] = authors

    # Extract pagination
    pagination = extract_pagination(article_element)
    article_data['pagination'] = pagination

    # Extract additional useful fields
    article_data['pmid'] = extract_pmid(article_element)
    article_data['abstract'] = extract_abstract(article_element)
    article_data['journal'] = extract_journal(article_element)
    article_data['publication_date'] = extract_publication_date(article_element)
    article_data['mesh_headings'] = extract_mesh_headings(article_element)
    article_data['publication_status'] = extract_publication_status(article_element)
    article_data['article_ids'] = extract_article_ids(article_element)

    return article_data


def extract_authors(article_element) -> List[Dict[str, str]]:
    authors = []
    author_list = article_element.find('.//AuthorList')

    if author_list is not None:
        for author in author_list.findall('Author'):
            author_info = {}

            # Last name
            last_name_elem = author.find('LastName')
            author_info[
                'last_name'] = last_name_elem.text.strip() if last_name_elem is not None and last_name_elem.text else ''

            # First name
            first_name_elem = author.find('ForeName')
            author_info[
                'first_name'] = first_name_elem.text.strip() if first_name_elem is not None and first_name_elem.text else ''

            # Middle name
            middle_name_elem = author.find('MiddleName')
            author_info[
                'middle_name'] = middle_name_elem.text.strip() if middle_name_elem is not None and middle_name_elem.text else ''

            # Full name (constructed)
            full_name_parts = [author_info['first_name'], author_info['middle_name'], author_info['last_name']]
            author_info['full_name'] = ' '.join([part for part in full_name_parts if part])

            authors.append(author_info)

    return authors


def extract_pagination(article_element) -> Dict[str, str]:
    pagination = {}

    pagination_elem = article_element.find('.//Pagination')
    if pagination_elem is not None:
        # MedlinePgn (page numbers)
        medline_pgn = pagination_elem.find('MedlinePgn')
        if medline_pgn is not None and medline_pgn.text:
            pagination['pages'] = medline_pgn.text.strip()

        # Start page
        start_page = pagination_elem.find('StartPage')
        if start_page is not None and start_page.text:
            pagination['start_page'] = start_page.text.strip()

        # End page
        end_page = pagination_elem.find('EndPage')
        if end_page is not None and end_page.text:
            pagination['end_page'] = end_page.text.strip()

    return pagination


def extract_pmid(article_element) -> str:
    """Extract PMID from the article."""
    pmid_elem = article_element.find('.//PMID')
    return pmid_elem.text.strip() if pmid_elem is not None and pmid_elem.text else ''


def extract_abstract(article_element) -> str:
    """Extract abstract from the article."""
    abstract_elem = article_element.find('.//AbstractText')
    return abstract_elem.text.strip() if abstract_elem is not None and abstract_elem.text else ''


def extract_journal(article_element) -> str:
    """Extract journal name from the article."""
    journal_elem = article_element.find('.//Journal/Title')
    return journal_elem.text.strip() if journal_elem is not None and journal_elem.text else ''


def extract_publication_date(article_element) -> Dict[str, str]:
    """Extract publication date from the article."""
    date_info = {}

    pub_date = article_element.find('.//PubDate')
    if pub_date is not None:
        year_elem = pub_date.find('Year')
        month_elem = pub_date.find('Month')
        day_elem = pub_date.find('Day')

        date_info['year'] = year_elem.text.strip() if year_elem is not None and year_elem.text else ''
        date_info['month'] = month_elem.text.strip() if month_elem is not None and month_elem.text else ''
        date_info['day'] = day_elem.text.strip() if day_elem is not None and day_elem.text else ''

    return date_info


def extract_mesh_headings(article_element) -> List[Dict[str, Any]]:
    """Extract MeSH headings from the article."""
    mesh_headings = []
    
    mesh_heading_list = article_element.find('.//MeshHeadingList')
    if mesh_heading_list is not None:
        for mesh_heading in mesh_heading_list.findall('MeshHeading'):
            heading_data = {}
            
            # Extract descriptor name
            descriptor_elem = mesh_heading.find('DescriptorName')
            if descriptor_elem is not None:
                heading_data['descriptor'] = {
                    'name': descriptor_elem.text.strip() if descriptor_elem.text else '',
                    'ui': descriptor_elem.get('UI', ''),
                    'major_topic': descriptor_elem.get('MajorTopicYN', 'N') == 'Y'
                }
            
            # Extract qualifier names
            qualifiers = []
            for qualifier_elem in mesh_heading.findall('QualifierName'):
                qualifier_data = {
                    'name': qualifier_elem.text.strip() if qualifier_elem.text else '',
                    'ui': qualifier_elem.get('UI', ''),
                    'major_topic': qualifier_elem.get('MajorTopicYN', 'N') == 'Y'
                }
                qualifiers.append(qualifier_data)
            
            heading_data['qualifiers'] = qualifiers
            mesh_headings.append(heading_data)
    
    return mesh_headings


def extract_publication_status(article_element) -> str:
    """Extract publication status from the article."""
    status_elem = article_element.find('.//PublicationStatus')
    return status_elem.text.strip() if status_elem is not None and status_elem.text else ''


def extract_article_ids(article_element) -> Dict[str, str]:
    """Extract article IDs from the article."""
    article_ids = {}
    
    article_id_list = article_element.find('.//ArticleIdList')
    if article_id_list is not None:
        for article_id in article_id_list.findall('ArticleId'):
            id_type = article_id.get('IdType', '')
            id_value = article_id.text.strip() if article_id.text else ''
            if id_type and id_value:
                # If the id_type already exists, append to it (comma-separated)
                if id_type in article_ids:
                    article_ids[id_type] = f"{article_ids[id_type]}, {id_value}"
                else:
                    article_ids[id_type] = id_value
    
    return article_ids
