""" Leap year"""
year = int(input("Enter an year :"))
if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 ==0)):
    print("leap year")
else:
    print("not leap year")


""" Print Pattern of half pyramid of stars"""
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

""" count total number of digits in a number"""
num = int(input("Enter a number :"))
num_str = str(num)
count = 0
for i in num_str:
    count = count+1
print(count)


