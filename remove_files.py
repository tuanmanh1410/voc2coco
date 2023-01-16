# Remove files with a given extension from a directory
# Usage: python remove_files.py <directory> <extension>
# Use this to automated deleting xml file after converting to json

import os
import sys

def remove_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            os.remove(os.path.join(directory, filename))

if __name__ == '__main__':
    remove_files(sys.argv[1], sys.argv[2])
