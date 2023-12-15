""" A function called itself """

""" factorial of a number"""
def fact(n):
    if n==1:
        print(n)
        return 1
    else:
        x= n* fact(n-1)
        print(x)
        return x
print("factorial:",fact(5))
print("_____________________________________")

""" sum of first 10 numbers"""
def counter(c):
    if c<=0:
        print(c)
        return c
    else:
        x=c+counter(c-1)
        print(x)
        return x
        #return c+counter(c-1)
print("Sum of first n numbers:",counter(10))
print("_____________________________________")

""" Another way"""
def another(k):
    if k>0:
        result = k+ another(k-1)
        print(result)
        return result
    else:
        result=0
        print(result)
    return result
print(another(5))
print("_____________________________________")

""" sum of digits"""
def digit_sum(n):
    if n==0:
        return 0
    else:
        digit = n%10
        sum = digit + digit_sum(int(n//10))
        return sum
result = digit_sum(34)
print(result)
print("_____________________________________")

def digit_pro(n):
    if n<=10:
        return 0
    else:
        digit = n%10
        pro = digit* digit_pro(n//10)
        return pro
#result1 = digit_pro(34)
print(digit_pro(234))
print("_____________________________________")

""" fibonacci"""
def fib(n):
     if n==0:
         print(n)
         return 0
     elif n==1:
         print(n)
         return 1
     else:
         f= (fib(n-1)+fib(n-2))
         print(f)
         return f

print(fib(5))
