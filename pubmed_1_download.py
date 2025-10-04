from core.downloader import download_files

download_files(
    urls=[f"https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/pubmed25n{i:04d}.xml.gz" for i in range(1, 2)],
    output_dir='./pubmed_data',
    max_files=None
)
