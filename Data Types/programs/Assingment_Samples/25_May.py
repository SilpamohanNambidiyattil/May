""" Python program to print the sum of digits of a number using while loop ????"""
num = int(input("Enter a number :"))
i = 1
sum = 0
while (i<=num):
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of digits :", sum)


""" Python program to print a series according to the common difference ???? """
print("________________________________________")
cd = int(input("Enter common difference  :"))
num1 = int(input("Enter  the limit of series :"))
next_num = 0
i = 1
while (i<=num1):
    print(next_num, end= ' ')
    next_num = next_num + cd
    i = i+1


""" Python program to check a number is perfect numberor not"""
print("\n________________________________________")
n = int(input("enter a number :"))
i= 1
sum_factor = 0
while (i<n):
    if (n % i == 0):
        sum_factor = sum_factor + i
    i = i+1
if sum_factor == n:
    print("Perfect number")
else:
    print("not perfect number")

