import os
import sys
# Name: Kyle Carnrite
# Date Started: January 12th
# Description: Takes target folder and deletes compressed folders
# WARNING: Do not use on folders you have important data. This program simply targets compressed folders

def emptyFolder(target):
    dirName = target
    for levels in os.walk(dirName, topdown=False):
        for directory in levels[1]: os.rmdir(levels[0] + levels[0])
        for fileToDelete in levels[2]:
            os.remove(levels[0] + fileToDelete)

