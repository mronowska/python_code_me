import os

# tylko pliki Pythonowe znajdujące się w tym folderze
def display_files_with_extension(extension):
    all_files = os.listdir()
    files_with_extension = []
    for f in all_files:
        if f.endswith(extension):
            files_with_extension.append(f)
    return files_with_extension

display_files_with_extension(".py")

# tylko komentarze we wszystkich plikach

def show_commeted_lines():
    python_files = display_files_with_extension(".py")
    for file in python_files:
        print(file)
        with open(file, mode="r", encoding="utf-8") as f:
            all_lines = f.readlines()
            for line in all_lines:
                if line.startswith("#"):
                    print(line, end="")

show_commeted_lines()