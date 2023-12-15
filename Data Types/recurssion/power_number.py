def number_power(n,x):
    if x==0:
        return 1
    else:
        y = n* number_power(n,x-1)
        return y
print("Power:",number_power(2,3))