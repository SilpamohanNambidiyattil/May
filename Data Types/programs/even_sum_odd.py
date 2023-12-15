check_list = [3,6,7,5,11,8]
print("Given list :", check_list)
even_list = []
odd_list = []
for i in  check_list :
    if (i % 2) == 0 :
        even_list.append(i)
    else :
        odd_list.append(i)
print("even list:", even_list)
print("odd list:", odd_list)
sum1 = 0
sum2 = 0
for i in even_list:
    #print(i)
    sum1 = sum1+i
print("sum of even  list :",sum1)
for i in odd_list:
    #print(i)
    sum2 = sum2+i
print("sum of odd list :",sum2)

