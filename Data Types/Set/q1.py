"""convert list of list in to list of sets????????"""

list_list = [[1,2,3], [4,5,6], [7,8,9]]
print("Given list of list:",list_list)
list_set = []
for i in list_list :
    list_set.append(set(i))
print("list of sets :", list_set)

print("******************************************************")

"""intersection of sets using & operator?"""
set1 = {1,2,3,4}
set2 = {2,3,4,5}
set3 = {6,5,4,3,2,1}
set4 = set1 & set2 & set3
print(set4)

print("********************************************************")
"""find an element inthe set?"""
set5 = {"apple","mango","cherry"}
print("apple" in set5)

