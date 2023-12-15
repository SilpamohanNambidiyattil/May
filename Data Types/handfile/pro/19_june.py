""" python program to convert lower case strings in to upper case """
with open(r'silpa.txt','r')as sil:
    string = sil.read()
    print(string)
    for i in string:
        x=string.upper()
    print(x)
    sil.close()


""" Reverse lines in the text file with reversing the words in the line and store in another file"""
file1 = open('output_file.txt','w')
with open('silpa.txt','r') as sil:
    words = sil.read()
rev = words[::-1]
file1.writelines(rev)
file1.close()
sil.close()

""" copy content of one file to another"""
f1 = open('copy_output.txt','w')
with open('silpa.txt','r') as sil:
    for i in sil:
        f1.write(i)
sil.close()