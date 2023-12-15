""" 1.Ask the user to enter the names of three people they want to invite to a party and store them in a list. Aft
er they have entered all three names, ask them if they want to add another. If they do, allow them to add
more names until they answer “no”. When they answer “no”, display how many people they have invited t
o the party. """

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

"""
OUTPUT
Enter name of three people:
silpa
sariga
sachu
['silpa', 'sariga', 'sachu']
If you wants to add another:yes
achu
If you wants to add another:yes
sagar
If you wants to add another:no
['silpa', 'sariga', 'sachu', 'achu', 'sagar']
"""
