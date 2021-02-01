import os
import sys
# Name: Kyle Carnrite
# Date Started: January 12th
# Description: Takes target folder and deletes compressed folders
# WARNING: Do not use on folders you have important data. This program simply targets compressed folders

def emptyFolder(target):
    targetName = target
    # Walk through the files and folders in the targeted directory.
    for levels in os.walk(targetName, topdown=False):
        for directory in levels[1]: 
            os.rmdir(levels[0] + '/' + directory)
        for fileToDelete in levels[2]:
            os.remove(levels[0] + '/' + fileToDelete)

# Takes first argument to dirName
dirName = sys.argv[1]
for levels in os.walk(dirName, topdown=True):
    if len(levels[1]) != 0:
        for folder in levels[1]:
            # If the folder has the extension .zip
            if folder.endswith('.zip'):
                #Check if the directory is empty
                if len(os.listdir(levels[0] + folder)) == 0:
                    os.rmdir(levels[0] + folder)
                else:
                    emptyFolder(levels[0] + folder)
                    os.rmdir(levels[0] + folder)

