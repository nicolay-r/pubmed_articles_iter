from collections import Counter
from os.path import basename
from tqdm import tqdm


def __filter_articles(articles_it, filter_func, ctr, pbar, current_file):
    for article in articles_it:
        if filter_func is not None and not filter_func(article):
            continue
        ctr['filtered'] += 1
        pbar.set_postfix(file=current_file, found=ctr['found'])
        yield article


def iter_articles(filepaths, desc, filter_func=None, fp_handler=None):
    """
    NOTE:
        - filter_func: is an optional parameter for filtering articles if needed.
        The filter itself is out of scope of the current repository.
    """
    ctr = Counter()
    with tqdm(filepaths, desc=desc) as pbar:
        for filepath in pbar:
            print(filepath)
            articles_it = fp_handler(file_path=filepath)
            filter_articles_it = __filter_articles(
                articles_it=articles_it,
                filter_func=filter_func,
                pbar=pbar,
                ctr=ctr,
                current_file=basename(filepath))

            for paper in filter_articles_it:
                yield paper