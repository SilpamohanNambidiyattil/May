list_items = ["apple", "orange", "mango", "grapes"]
print(list_items)
print(list_items[2]) #display 2nd item
print(list_items[-1]) #display last item
print(list_items[:2]) # display first 2 positioned items
print(list_items[2:]) # display from mango only
print(list_items[1:]) # display from orange only
print(list_items[0][-1]) # e from apple

print(list_items[3][::2])
print(list_items[3][::3])
print(list_items[3][-1])
print(list_items[3][:-1])


# Replace
list_items[1] = "pineapple"
print(list_items)
print(list_items[2][-2])



# in strings
str1 = "Hi dears"
x = list(str1) # convert given string to list
print(x)
x[1] = "v" # replace i to v
print(x)
print("".join(x)) # join the replaces list to string

list_items = ["apple", "orange", "mango", "grapes", ["python", "django", "react", "java"]]
print(list_items[4])
print(list_items[4][0])
print(list_items[4][0][0])
list_items[4][1] = "angular" # this replaces django to angular
print(list_items)
list_items.append("vue.js") # this append new element to the list
print(list_items)
list_items[4].insert(1, "golang") # this will add new item to a specific position
print(list_items)

# Remove Pop
list_items.remove("apple") #remove apple from the list
print(list_items)
list_items.pop(1)
print(list_items)

#list_items.clear()
#print(list_items)
#del list_items
#print(list_items)



# copy
x = list_items.copy()
print(x)

# reverse
list_items.reverse()
print(list_items)

#count
y = list_items.count("grapes")
print(y)

# extend
list_items1 = ["c", "c++"]
list_items.extend(list_items1)
print(list_items)

#Sort
list_so = ["silpa", "akshay", "latha", "mohan"] #cannot sort nested list
list_so.sort()
print(list_so)

#list_items[4].sort()
#print(list_items)

list_so.sort(reverse=True)
print(list_so)

list_so.sort(reverse=False)
print(list_so)
