from core.pubmed_parser import pubmed_papers_it
from core.utils_filter import iter_articles
from utils import write_jsonl, iter_dir_filepaths

write_jsonl(
    file_path=f"pubmed.jsonl",
    records_it=iter_articles(
        filepaths=iter_dir_filepaths(root_dir='./pubmed_data'),
        filter_func=None,
        desc="pubmed_data",
        fp_handler=pubmed_papers_it,
    )
)