import json
x = '{"name":"reethu", "age": 28 , "course": "python" , "guide": "priya"}'
print(x)
y = json.loads(x)
print(y['age'],y['course'])
