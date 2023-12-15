dict1 = {"name":"silpa", "age":25, "place":"abc", "course":"python"}
print(dict1)
# Acessing elments
print(dict1["name"])
print(dict1["course"])
print(dict1.get("name"))
# replace silpa with akshay
dict1["name"] = "akshay"
print(dict1)
dict1.update({"course":"react"})
print(dict1)
dict1.update({"qualification":"btech", "role":"training"}) #addds new items also
print(dict1)

x = dict1.keys()
print(x)
y = dict1.values()
print(y)

dict1.pop("name")
print(dict1)
dict1.popitem()
print(dict1)


z=dict1.copy()
print(z)
q =0
w= dict.fromkeys(z,q)
print(w)

e= dict1.setdefault("place","malappuram")
print(e)
print(dict1)

dict1['class'] = dict1.pop('course')
print(dict1)

keys = ["ten","twenty","thirty"]
values = [10,20,30]
new_dict = dict(zip(keys,values))
print(new_dict)

#merge two dict use update














