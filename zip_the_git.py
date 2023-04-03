#! python3
# zip_the_git.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments with date.

import zipfile, os
from datetime import date

def backupToZip(folder):
# Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)   # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    today = date.today()
    the_date = today.strftime("%d-%m-%Y")

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + the_date + '_' + str(number) + '.zip' 
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)


    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))

        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print('Done.')

backupToZip('/Users/joshuachristiansen/Github Work')
