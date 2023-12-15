""" Python program to count number of lines in a text file"""
with open(r'silpa.txt','r')as lc:
    lines = (len(lc.readlines()))
    print("no: of lines :",lines)
    lc.close()
