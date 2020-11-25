import os


def display_max_file():
    max_file_name = ''
    max_size = 0

    for file in os.listdir():
        current_size = os.path.getsize(file)
        if current_size > max_size:
            max_size = current_size
            max_file_name = file

    return max_file_name

print(display_max_file())