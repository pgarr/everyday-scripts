import datetime
import os
import shutil

BACKUP_THIS_DIRS = ("D:\pgarr",)


def backup_directory(main_dir):
    now = datetime.datetime.today().strftime('%Y-%m-%d')
    return os.path.join(main_dir, "BACKUP", now)


main_dir = input("Please enter main directory:")
directory = backup_directory(main_dir)

print(directory)

try:
    for dir_ in BACKUP_THIS_DIRS:
        shutil.copytree(dir_, directory)
except FileNotFoundError as e:
    print(e)
