"""Print first 10 numbers using while loop"""
i = 1
while i<=10:
    print(i, end=' ')
    i = i+1

num = int(input("\nEnter number of natural numbers :"))
j = 1
sum = 0
while j<=num:
    #n = int(input())
    sum = sum+j
    j =j +1
print("Sum of natural numbers :", sum)
