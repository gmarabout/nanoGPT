import os
import hashlib

def get_all_file_paths_recursively(path):
    """Get the list of paths of all files in all directories recursively."""
    file_paths = []
    for root, _, files in os.walk(path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def compute_file_hash(hash_obj, file_path):
    """Compute the hash of the contents of a given file."""
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return

file_paths = sorted(get_all_file_paths_recursively('input'))

hash_obj = hashlib.sha256()
for file_path in file_paths:
    if file_path == "input/integrity_check/checksum":
        continue
    compute_file_hash(hash_obj, file_path)

actual_checksum = hash_obj.hexdigest()
expected_checksum = open("input/integrity_check/checksum", "r").read().strip()
if actual_checksum != expected_checksum:
    raise ValueError(f"Checksum mismatch: expected {expected_checksum}, got {actual_checksum}")
