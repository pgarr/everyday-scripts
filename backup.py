import datetime
import logging
import os
import zipfile

BACKUP_THIS_DIRS = (
    "D:\pgarr\Documents", "D:\pgarr\instalki", "D:\pgarr\Music", "D:\pgarr\Pictures", "D:\pgarr\pobrane",
    "D:\pgarr\Videos")


# BACKUP_THIS_DIRS = ("D:\pgarr\Documents\praca",)  # for tests


def backup_directory(this_dir):
    now = datetime.datetime.today().strftime('%Y-%m-%d')
    back_dir = os.path.join(this_dir, "BACKUP", now)
    if not os.path.exists(back_dir):
        os.makedirs(back_dir)
    return back_dir


def zip_this_dir(path, zipped_file):
    for root, dirs, files in os.walk(path):
        if root.replace(path, '') == '':
            prefix = ''
        else:
            prefix = root.replace(path, '') + '/'
            if prefix[0] == '/':
                prefix = prefix[1:]
        for file in files:
            actual_file_path = root + '/' + file
            zipped_file_path = prefix + file
            try:
                zipped_file.write(actual_file_path, zipped_file_path)
            except Exception as e:
                logging.warning("Unable to backup file '%s'" % actual_file_path)
                logging.warning("Reason: %s, %s" % (e.__class__.__name__, e))
                continue
            logging.info("File '%s' stored" % actual_file_path)


def make_zip(folder_to_zip, destination, zip_file_name):
    logging.info("Storing folder: %s" % folder_to_zip)
    with zipfile.ZipFile(os.path.join(destination, zip_file_name), 'w', zipfile.ZIP_DEFLATED) as zipped_file:
        zip_this_dir(folder_to_zip, zipped_file)


logging.basicConfig(level=logging.INFO)  # TODO: lepsze logi, data, godzina, itp.
main_dir = input("Please enter backups main directory:")
directory = backup_directory(main_dir)

for dir_ in BACKUP_THIS_DIRS:
    name = os.path.basename(dir_) + '.zip'
    make_zip(dir_, directory, name)
