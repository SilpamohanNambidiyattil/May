""" 3.Write a Python program to check the validity of passwords input by users. 
{length of password should be between 6 to 16,atleast one small letter,One capital letter,one digit,and on
e special character}"""

password = input('Enter your password :')
print('Given password :',password)
low=0
up=0
digi=0
spe=0
if len(password)>=6 and len(password)<=16 :
    for i in password:
        if i.islower()==True:
            low=low+1
        if i.isupper()==True:
            up=up+1
        if i.isdigit()==True:
            digi=digi+1
        if i in '!@#$%&*_':
            spe=spe+1
if low>=1 and up>=1 and digi>=1 and spe>=1 :
    print('Valid password')
else :
    print('Invalid pssword')

""" 
OUTPUT:1
Enter your password :Silpamohan@97
Given password : Silpamohan@97
Valid password

OUTPUT:2
Enter your password :silpa
Given password : silpa
Invalid pssword 
"""

            