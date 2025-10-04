import json
from os import walk
from os.path import join


def iter_jsonl(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON line: {e}")
                    continue
                    
def write_jsonl(file_path, records_it):
    print(f"Writing: {file_path}")
    with open(file_path, "w", encoding="utf-8") as f:
        for record in records_it:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

def iter_dir_filepaths(root_dir):
    for (dirpath, _, filenames) in walk(root_dir):
        for filename in filenames:
            yield join(dirpath, filename)