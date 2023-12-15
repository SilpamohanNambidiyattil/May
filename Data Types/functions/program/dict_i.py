print("Set Default")
n=int(input("Enter limit : "))
dict1 = {}
for i in range(1,n+1):
    dict1.setdefault(i,i*i)
print(dict1)

print("________________________")
print("Zip")
dict2 = {}
keys = []
values = []
for i in range(1, n + 1):
    keys.append(i)
    #print(keys)
    values.append(i*i)
    #print(values)
    dict2 = dict(zip(keys,values))
print(dict2)


print("________________________________")
