num = int(input("Enter a number :"))
sum = 0
temp = num
while (temp>0):
    digit = temp%10 # last digit fetch 3
    sum = sum + (digit**3) #0 + (cube of3)
    temp = temp//10# fetch 15 then loop will continue
if (num==sum):
    print("amstrong")
else:
    print("not amstrong")