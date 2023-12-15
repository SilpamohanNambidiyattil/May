""" Python program to check a file is existing or not  """

import os

file_path = r'../base1.py'
x = os.path.exists(file_path)
if x :
    print(f' {file_path} The file is existing')
else:
    print(f' The file {file_path} is not existing')