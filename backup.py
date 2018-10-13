import datetime
import os
import shutil

BACKUP_THIS_DIRS = ("D:\pgarr",)

main_dir = input("Please enter main directory: ") # TODO: walidacja podanej ścieżki
now = datetime.datetime.today().strftime('%Y-%m-%d')
directory = os.path.join(main_dir, "BACKUP", now)

print(directory)

for dir_ in BACKUP_THIS_DIRS:
    shutil.copytree(dir_, directory)
