def cal_lcm(x,y):
    if x > y:
        greatest = x
    else:
        greatest = y
    while (True):
        if (greatest % x == 0) and (greatest % y == 0):
            lcm = greatest
            break
        greatest = greatest+1
    return lcm
n1 = int(input("enter  1st number:"))
n2 = int(input("enter 2nd number :"))
print("lcm :", cal_lcm(n1,n2))