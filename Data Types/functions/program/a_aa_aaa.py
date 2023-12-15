a = input("Enter the value:")
#a = int(input("Enter the value :"))
a_list = []
for i in range(1,5):
    a_list.append(str(a*i).split(' '))
print(a_list)
num = 0
for i in a_list:
    num = (num*10)+(ord(i)-48)
    print(ord(i))
print(num)
