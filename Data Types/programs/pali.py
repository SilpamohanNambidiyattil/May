num = int(input("Enter a number :"))
rev = 0
temp = num
while (num>0):
    rem = num%10
    #print(rem)
    rev = (rev*10)+rem
    #print(rev)
    num = num//10
if (rev==temp):
    print("pali")
else:
    print("not")


