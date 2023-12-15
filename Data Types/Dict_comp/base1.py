""" Syntax
        dictionary = {key:value for vars in iterable}"""
square_dict = {}
for num in range(1,11):
    square_dict[num] = num*num
print(square_dict)
square_dict1 = {num:num*num for num in range(1,11)}
print("dict_comp:", square_dict1)

old_price = {'milk':1.02, 'coffee':2.5, 'bread':2.5}
dollar_to_pound = 0.76
new_price = {key:value*dollar_to_pound for (key,value) in old_price.items()}
print(new_price)

first_dict = {'jack':38, 'jin':48, 'rose':57}
even_dict = {k:v for (k,v) in first_dict.items() if v%2==0}
print(even_dict)

keys = ['a','b','c','d','e','f']
values = [1,2,3,4,5]
newd = {keys:values for (keys,values) in zip(keys,values)}
print(newd)

dict_new = {key:('even' if key%2==0  else "odd") for key in range(1,11) }
print(dict_new)



ke = ['a','b','c','d','e','f']
new__ = {ke[i]:ke[i+1] for i in range(0,len(ke),2)}
print(new__)

ke = ['a','b','c','d','e','f']
new1 = {ke[i] for i in range(0,len(ke),2)}
new2 = {ke[j] for j in range(1,len(ke),2)}
print(dict(zip(new1,new2)))


