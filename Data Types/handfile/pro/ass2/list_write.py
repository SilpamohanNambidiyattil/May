""" Python program to Writing list to a file """
list1 = ['mango', 'apple', 'grape', 'pineapple', 'chakka',2]
with open('item_list.txt', 'w')as sill:
    for i in list1:
        sill.write(str(i)+'\n')
sill.close()