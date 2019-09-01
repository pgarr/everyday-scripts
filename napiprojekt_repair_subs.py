# -*- coding: utf-8 -*-

import os

filepath = "C:\\Users\\pgarr\\Desktop\\baba.txt"

dictionary = {
    "¹": "ą",
    "æ": "ć",
    "ê": "ę",
    "³": "ł",
    "ñ": "ń",
    # "": "ó",
    "œ": "ś",
    "Ÿ": "ź",
    "¿": "ż",
    # "": "Ą",
    # "": "Ć",
    # "": "Ę",
    "£": "Ł",
    # "": "Ń",
    # "": "Ó",
    "Œ": "Ś",
    # "": "Ź",
    "¯": "Ż"
}


def replace_all_bad_characters(string):
    for key, value in dictionary.items():
        string = string.replace(key, value)
    return string


filename, file_extension = os.path.splitext(filepath)
new_filename = "repaired_subs"

new_filepath = os.path.join(os.path.dirname(filepath), new_filename + file_extension)

with open(new_filepath, 'a', encoding="utf-8") as new_file:
    with open(filepath, encoding="utf-8") as old_file:
        data = old_file.read()
        data = replace_all_bad_characters(data)
        new_file.write(data)
