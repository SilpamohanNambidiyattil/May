""" Specific line from a text file """

with open(r'silpa.txt','r')as lc:
    lines = lc.readlines()
    print("no:of lines:",len(lines))
    line_no = int(input("Enter line number:"))
    print(lines[line_no])
    lc.close()