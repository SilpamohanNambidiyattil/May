""" 9.Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the na
mes and after each name display “[name] has been invited”. If they enter a number which is 10 or higher,
display the message “Too many people”. """

n=int(input('Enter how many people user wants to invite :'))
if (n<10):
    for i in range(0,n):
        name=input('Enter the name :')
        print(f'{name} has been invited')
elif n>10:
    print('Too many people')

""" 
OUTPUT1
Enter how many people user wants to invite :2
Enter the name :silpa
silpa has been invited
Enter the name :reethu
reethu has been invited

OUTPUT2
Enter how many people user wants to invite :11
Too many people
"""