""" 6.Display the following message:{1:square 
2:Triangle 
entrer a number} . If the user enters 1, then it should ask them for the length of one 
of its sides and display the area. If they select 2, it should ask for the base and height of the triangle and d
isplay the area. If they type in anything else, it should give them a suitable error message."""

def square():
    l=int(input('Enter the length :'))
    area=l*l
    print('Area of Square :',area)
def triangle():
    b=int(input('Enter the base length :'))
    h=int(input('Enter the height :'))
    area=(1/2)*b*h
    print('Area of Triangle :',area)
while True:
    select=input('Enter your choice: 1. Square 2. Triangle')
    if select=='1':
        square()
    elif select=='2':
        triangle()
    else:
        print('Invalid')

""" 
OUTPUT
Enter your choice: 1. Square 2. Triangle1
Enter the length :2
Area of Square : 4
Enter your choice: 1. Square 2. Triangle2
Enter the base length :4
Enter the height :6
Area of Triangle : 12.0
Enter your choice: 1. Square 2. Triangle3
Invalid
"""