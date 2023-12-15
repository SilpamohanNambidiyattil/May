num = int(input("Enter a number :"))
def fact_num(num):
    if (num < 0):
        return 0
    elif (num == 0) or (num == 1):
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * num
            num = num - 1
        return fact
print("Factorial : ", fact_num(num))