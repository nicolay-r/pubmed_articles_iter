from os import walk
from os.path import join


def iter_dir_filepaths(root_dir):
    for (dirpath, _, filenames) in walk(root_dir):
        for filename in filenames:
            yield join(dirpath, filename)
