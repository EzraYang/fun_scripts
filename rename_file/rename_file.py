import os
import re

def clean_coursera_file(f):
    '''os.rename(old_name, new_name)'''
    os.rename(os.path.join(path, f), os.path.join(path, f[34:]))

# modify path before run script
path = input('Enter the path: ')

for file in os.listdir(path):
    if re.search(r'^_[a-z0-9]+_', f) != None & len(re.findall(r'^_[a-z0-9]+_', f)[0]) == 34:
        clean_coursera_file(file)
