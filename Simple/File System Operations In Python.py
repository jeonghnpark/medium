import os
print(f"{os.getcwd()}")
path="sample_data"
if not os.path.exists(path):
    os.mkdir('sample_data')
if os.path.exists(path):
    print(f'{path} exists')
else:
    print(f"{path} doesn't exists")

#saft way to make path, independent on OS

print(os.path.exists(os.path.join(path,'README.md')))

#show directory contents
print(os.listdir(path))

#file search
from glob import glob
print(list(glob(os.path.join(path, "*.csv"))))