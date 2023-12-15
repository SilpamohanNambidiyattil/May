""" Python program to display multiplication table of a number ? """
print("MULTIPLICATION TABLE PROGRAM")
print("-----------------------------")
num = int(input("Enter a number :"))

for i in range(0,11):
    Mul = num*i
    print(num,'x',i,'=',Mul )


""" Python program to find factorial of a number ?"""
print("FACTORIAL PROGRAM")
print("-----------------------------")
num1 = int(input("Enter a number :"))
if (num1<0):
    print("No Factorial")
elif (num1==0) or (num1==1):
    print("Factorial of 0 is 1")
else :
    fact = 1
    for i in range(1, num1 + 1):
        fact = fact*num1
        num1 = num1-1
    print("Factorial :",fact)

""" Python program to find sum of N natural numbers ? """
print("SUM OF NATURAL NUMBERS ")
print("---------------------------------")
num2 = int(input("Enter number of natural numbers :"))
sum = 0
for i in range(num2):
    n = int(input())
    sum = sum+n
print("Sum of natural numbers :", sum)


