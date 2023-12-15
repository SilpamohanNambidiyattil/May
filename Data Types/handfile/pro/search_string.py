""" Search a string"""

with open(r'silpa.txt','r')as lc:
    string = lc.read()
    print(string)
    check_str = input("Enter a string :")
    if check_str in string:
        print(check_str,'is found')
    else:
        print(check_str," is not found")

    lc.close()
