""" 10.Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, dis
play “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”. """

print('Enter your choice : 1,2,3')
n=int(input('Enter a number:'))
if n==1:
    print('Thank you')
elif n==2:
    print('Well Done')
elif n==3:
    print('Correct')
else:
    print('Error message')

""" 
OUTPUT1
Enter your choice : 1,2,3
Enter a number:1
Thank you

OUTPUT2
Enter your choice : 1,2,3
Enter a number:2
Well Done

OUTPUT3
Enter your choice : 1,2,3
Enter a number:3
Correct

OUTPUT4
Enter your choice : 1,2,3
Enter a number:5
Error message
"""