"""Find the minimum and maximum numbers in a list ?"""

n = int(input("Enter list limit :"))
num_list =[]
for i in range(1, n+1):
    num = int(input())
    num_list.append(num)
max_value = 0#int('-inf')
min_value = -1#int('inf')
for i in num_list:
    if i > max_value:
        max_value= i
    if i <min_value:
        min_value=i
print("maximum value :",max_value)
print("minimum value :",min_value)
