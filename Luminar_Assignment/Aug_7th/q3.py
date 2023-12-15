""" 3.Using the below list ask the user which row they would like displayed and display just that row. Ask the
m to enter a new value and add it to the end of the row and display the row again. list=[[2,5,8],[3,7,4],[1,6,
9],[4,2,0]] """

list_1=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
ask=int(input('Enter which row you would like to displayed:'))
print(list_1[ask])
new_list=list_1[ask]
new_val=int(input('Enter a new value to the row:'))
new_list.append(new_val)
print('After appending:',new_list)

"""
OUTPUT
Enter which row you would like to displayed:2
[1, 6, 9]
Enter a new value to the row:5
After appending: [1, 6, 9, 5]
"""
