"""Convert the string "123" into 123 without using built-apl int() ?"""
n = input("Enter a number string  :")
#n = "123"
num = 0
l = len(n)
for i in n:
    num = (num*10)+(ord(i)-48)
    #print(ord(i))
print(num)

