""" 5.Adapt the above program to display the names and ages of all the people in the list but do not show thei
r Id. """

people=[]
for i in range(4):
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    id=input("Enter your id: ")
    people.append({"name":name,"age":age,"id":id})

for p in people:
    print(f"Name: {p['name']}, Age:{p['age']}")


"""
OUTPUT
Enter your name: silpa
Enter your age: 25
Enter your id: 1
Enter your name: reethu
Enter your age: 29
Enter your id: 2
Enter your name: aruna
Enter your age: 25
Enter your id: 3
Enter your name: mustha
Enter your age: 26
Enter your id: 4
Name: silpa, Age:25
Name: reethu, Age:29
Name: aruna, Age:25
Name: mustha, Age:26
"""