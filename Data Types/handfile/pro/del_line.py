with open(r'myfile.txt','r')as  sill:
    lines = sill.readlines()
    line_index = 1
    line_no = int(input("Enter line no:"))
    with open('myfile.txt','w')as sill:
        for i in lines:
            if  line_no != line_index:
                sill.write(i)
                line_index= line_index+1
            #line_index=line_index+1
new_file = open('myfile.txt','r')
for i in  new_file:
    print(i)

sill.close()