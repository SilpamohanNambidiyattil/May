""" File handling
* modes of file
    1 create (x)
    2 write (w)
    3 read (r)
    4 delete (remove)
    5 add (append)

    Syntax : variable = open('file name . ext', mode)
    """
""" Creating file"""
#file = open('myfile.txt', 'x')
#print(file)
#file.close()

""" Write to file"""
file = open('pro/Assignment/myfile.txt', 'w')
file.write("hai silpa ")
file.close()

""" Reading file"""
file = open('pro/Assignment/myfile.txt', 'r')
print(file.read())
file.close()

""" Append used to overwrite"""
file = open('pro/Assignment/myfile.txt', 'a')
file.write("How are you")
file.close()
file = open('pro/Assignment/myfile.txt', 'r')
print(file.read())
file.close()

""" Another method : with open
    close file inside  the function
    """
with open('pro/Assignment/myfile.txt', 'r') as file:
    print(file.read())
    file.close()
with open('pro/Assignment/myfile.txt', 'a') as file:
    file.write("helooo")
    file.close()


""" Remove file"""
import os
file1 = open('myfff.txt','x')
print(file1)
os.remove('myfff.txt')



