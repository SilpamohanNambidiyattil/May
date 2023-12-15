""" Access the value of key2 from the following JSON """
import json
x = '{"name":"silpa", "age":25, "course":"python"}'
print(x)
y = json.loads(x)
print("json to python :",y)
print(y['age'])
