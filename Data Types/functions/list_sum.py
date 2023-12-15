num = [6,8,5,3,2,1]
def list_sum(num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum
print("Sum of  list elements :", list_sum(num))