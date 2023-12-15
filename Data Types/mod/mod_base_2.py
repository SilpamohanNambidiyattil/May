""" json module"""
""" java script object notation"""
""" json is used for storing and exchanging datas """
""" dumps() is used to convert python(dict format) to json(string format  but looks like dict)"""
""" loads() is used to convert json to python"""


import json
x = {'name':'silpa', 'age':25, 'course':"python"}
print(x)
print(type(x))
y = json.dumps(x)
print("Python to json :",y)
print(type(y))
#print(y['age'])

x1 = '{"name":"silpa", "age":25, "course":"python"}'
print(x1)
print(type(x1))
y1 = json.loads(x1)
print("json to python:",y1)
print(type(y1))
print(y["age"])

""" dir() is used to list the functionality provided by json"""
func = dir(json)
print(func)

