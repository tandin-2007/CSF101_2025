import os

def file_exists(filename):
    return os.path.exists(filename)

print(f"'sample.txt' exists: {file_exists('sample.txt')}")
print(f"'nonexistent.txt' exists: {file_exists('nonexistent.txt')}")
import os

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

rename_file('sample.txt', 'renamed_sample.txt')
print("File renamed successfully.")
print(f"'renamed_sample.txt' exists: {file_exists('renamed_sample.txt')}")