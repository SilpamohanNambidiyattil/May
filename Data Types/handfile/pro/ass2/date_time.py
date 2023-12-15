""" Python program to get file creation and modification date_time """

import os.path, time
newfile = open('sample.txt','w')
newfile.write("hai hello")
print("created time :", time.ctime(os.path.getctime('sample.txt')))
print("last modified time :", time.ctime(os.path.getmtime('sample.txt')))