""" 4.Ask the user to enter the name, age and Id for four people. Ask for the name of one of the people in the
list and display their age and Id. """

people=[]
for i in range(4):
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    id=input("Enter your id: ")
    people.append({"name":name,"age":age,"id":id})

display=input("Enter the name of the person from the list: ")
for p in people:
    if p["name"]==display:
        print(f"Age: {p['age']},ID:{p['id']}")

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
Enter your age: 25
Enter your id: 4
Enter the name of the person from the list: reethu
Age: 29,ID:2
"""
