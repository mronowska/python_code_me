import os

def display_files_without_extension():
    all_files = os.listdir()
    files_without_extension = []
    for f in all_files:
        if f.find('.') == -1:  # found
            files_without_extension.append(f)

    return files_without_extension

print(display_files_without_extension())
