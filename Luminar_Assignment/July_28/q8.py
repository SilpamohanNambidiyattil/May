""" 8.Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, displ
ay the message “You can learn to drive”, if they are 16, display the message“You can buy a lott
ery ticket”,if they are under 16, display the message “You can go for treat”. """

age =int(input('Enter age:'))
if age>=18:
    print('You can vote')
elif age==17:
    print('You can learn to drive')
elif age==16:
    print('You can buy a lottery ticket')
else:
    print('You can go for treat')

""" 
OUTPUT1
Enter age:18
You can vote

OUTPUT2
Enter age:17
You can learn to drive

OUTPUT3
Enter age:16
You can buy a lottery ticket

OUTPUT4
Enter age:5
You can go for treat
"""