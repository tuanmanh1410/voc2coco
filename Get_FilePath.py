# Get the file *xml path in folder and store in txt file
import os
import glob
import sys

# Get the file *xml path in folder and store in txt file
def get_file_path(path, file_type):
    with open('file_path.txt', 'w') as f:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(file_type):
                    f.write(os.path.join(root, file) + '\n')
#main
if __name__ == '__main__':
    path = sys.argv[1]
    file_type = sys.argv[2]
    get_file_path(path, file_type)