import init
import csv

def write_tab_to_file(filename,  tab = []):
    with open(filename, mode="w", encoding="utf-8") as file:
        for i in tab:
            file.writelines(i + ', ')

def read_file(filename, index):
    with open(filename, encoding="utf-8") as my_file:
        text = my_file.read()
        songs = text.split(", ")
        return songs[index]