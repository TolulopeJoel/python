# os module

import os

# current working directory
folder = os.getcwd()
print(folder)

# list files
folder_contents = os.listdir('/Users/tolu/Documents/Projects/Coding/Teaching')
print(folder_contents)


# make directory
new = os.mkdir('mark')

print(os.getcwd())

# change directory
os.chdir('mark')

print(os.getcwd())


os.rename('something.txt', 'old.txt')
os.remove('old.txt')

os.rmdir('mark')
