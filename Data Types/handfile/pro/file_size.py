""" Python program to check file size"""
import os
file = open('silpa.txt','a')
file.write("")
file.close()
file_size = os.path.getsize('silpa.txt')
print("file size is :", file_size,"bytes")