import os
import shutil

mysource_folder = r'C:\Users\Alex\Documents\Cousera\coursera-dl\cybersecurity-for-everyone'
mydestination_folder = r'C:\Users\Alex\Documents\Cousera\Cybersecurity_merged'


# Loop through all files and subdirectories in source folder and delete non .txt files
for subdir, dirs, files in os.walk(mysource_folder, topdown=False):
    for file in files:
        if not file.endswith('.txt'):
            os.remove(os.path.join(subdir, file))

    # Remove empty subdirectories
    if len(os.listdir(subdir)) == 0:
        os.rmdir(subdir)

#Place all files into a single folder
#for subdir, dirs, files in os.walk(mysource_folder):
    #for file in files:
        #shutil.copy2(os.path.join(subdir, file), mydestination_folder)