import os
from shutil import copyfile

pic_files = os.listdir('pages/art')

for file in pic_files:
    source = 'pages/art/' + file
    destination = ''
    if not os.path.isdir(source):
        with open(source, 'r') as read_file:
            if 'short' in read_file.read():
                destination = 'pages/art/s/' + file
            else:
                destination = 'pages/art/l/' + file
        copyfile(source, destination)
