check_list = [50, 2, 1, 9]
#check_list = list('50219')
new_list = []
#print(len(check_list))
#str1 = str(check_list)
#print(str1)
#length = len(str1)
length = len(check_list)
print(length)
if length==0:
    print('')
if length==1:
    print(check_list)
for i in range(length):
    m = check_list[i]
    rem = check_list[:i]+check_list[i+1:]
    for j in range(i+1):
        new_list.append([rem])
print(new_list)
