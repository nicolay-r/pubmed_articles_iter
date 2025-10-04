from core.pubmed_parser import pubmed_papers_it
from core.utils import iter_dir_filepaths
from core.utils_filter import iter_articles
from core.utils_jsonl import write_jsonl

write_jsonl(
    file_path=f"pubmed.jsonl",
    records_it=iter_articles(
        filepaths=iter_dir_filepaths(root_dir='./pubmed_data'),
        filter_func=None,
        desc="Converting PubMed XML to JSONL",
        fp_handler=pubmed_papers_it,
    )
)