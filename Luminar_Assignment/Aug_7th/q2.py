""" 2.Change the above question so that once the user has completed their list of names, display the full list a
nd ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they answer “no”, delete
that entry from the list and display the list again. """

people=[]
print('Enter name of three people:')
for i in range(0,3):
    name=input()
    people.append(name)
print(people)
def add_another():
    add_name=input()
    people.append(add_name)
def display():
    print(people)

while True :
    ask=input('If you wants to add another:')
    if ask=='yes':
        add_another()
    elif ask=='no':
        display()
        break
    else:
        print('invalid')
one_name=input('Enter one name from the list:')
for i in people:
    if i==one_name:
        print(f'Position of {one_name} in the list is:',people.index(one_name))
        while True:
            entry=input('If you want to come this person to the party:')
            if entry=='no':
                people.remove(one_name)
                print(people)
                break

"""
OUTPUT
Enter name of three people:
silpa
reethu
aruna
['silpa', 'reethu', 'aruna']
If you wants to add another:yes
abin
If you wants to add another:yes
mustha
If you wants to add another:no
['silpa', 'reethu', 'aruna', 'abin', 'mustha']
Enter one name from the list:abin
Position of abin in the list is: 3
If you want to come this person to the party:no
['silpa', 'reethu', 'aruna', 'mustha']
"""
