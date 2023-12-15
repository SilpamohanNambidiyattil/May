dict1 = {"name1":"silpamohan","age1":25,"name2":"reethu","name2":"reethu","age2":25}
#dict1 = {"name":"priya","age":12,"place":"priya","course":"python"}
k = dict1.keys()
print(k)
v = dict1.values()
print(v)
x = []
for i in v :
    if i  not in x :
        x.append(i)
print("duplicates removed :", x)
new_dict = dict(zip(k,x))
print(new_dict)