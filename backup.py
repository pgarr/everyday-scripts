import datetime
import os
import shutil
import zipfile

# BACKUP_THIS_DIRS = ("D:\pgarr",)
BACKUP_THIS_DIRS = ("D:\pgarr\Documents\praca",)


def backup_directory(this_dir):
    now = datetime.datetime.today().strftime('%Y-%m-%d')
    back_dir = os.path.join(this_dir, "BACKUP", now)
    if not os.path.exists(back_dir):
        os.makedirs(back_dir)
    return back_dir


def zip_this_dir(path, zipped_file):
    for root, dirs, files in os.walk(path):
        for file in files:
            zipped_file.write(os.path.join(root, file), os.path.basename(os.path.normpath(path)) + "\\" + file)


def make_zip(folder_to_zip, destination, zip_file_name):
    zipped_file = zipfile.ZipFile(os.path.join(destination, zip_file_name), 'w', zipfile.ZIP_DEFLATED)
    zip_this_dir(folder_to_zip, zipped_file)
    zipped_file.close()


main_dir = input("Please enter backups main directory:")
directory = backup_directory(main_dir)

for dir_ in BACKUP_THIS_DIRS:
    make_zip(dir_, directory, 'zipfile.zip')

    #
    # try:
    #     for dir_ in BACKUP_THIS_DIRS:
    #         zip_path = os.path.join(directory, 'Python.zip')
    #         zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    #         zipdir(dir_, zipf)
    #         zipf.close()
    # except FileNotFoundError as e:
    #     print(e)
