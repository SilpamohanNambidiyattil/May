""" 4.Write a Python program to check if a triangle is equilateral, isosceles or scalene. and show its area and 
perimeter."""

x=int(input('Enter length of  x side :'))
y=int(input('Enter length of y side :'))
z=int(input('Enter length of z side :'))
def check(x,y,z):
    if x == y == z:
        area =(1/4)*(3)**(1/2)*x*x
        peri = 3*x
        print('Area of Equilateral Triangle:',area)
        print('Perimeter of Equilateral Triangle :',peri)
    elif x==y or  y==z or z==x:
        print('Isoceles Triangle')
        base=int(input('Enter base length :'))
        height=int(input('Enter height :'))
        area_i = (1/2)*base*height
        peri_i=(2*x)+y
        print('Area of Isoceles Triangle',area_i)
        print('Perimeter of Isoceles Triangle:',peri_i)
    else:
        print('Scalene Triangle')
        base_s=int(input('Enter base length :'))
        height_s=int(input('Enter height :'))
        area_s = (1/2)*base_s*height_s
        peri_s=x+y+z
        print('Area of Scalene Triangle',area_s)
        print('Perimeter of Scalene Triangle:',peri_s)
check(x,y,z)

"""  
OUTPUT1
Enter length of  x side :5
Enter length of y side :5
Enter length of z side :5
Area of Equilateral Triangle: 10.825317547305481
Perimeter of Equilateral Triangle : 15

OUTPUT2
Enter length of  x side :5
Enter length of y side :5
Enter length of z side :2
Isoceles Triangle
Enter base length :2
Enter height :6
Area of Isoceles Triangle 6.0
Perimeter of Isoceles Triangle: 15

OUTPUT3
Enter length of  x side :2
Enter length of y side :4
Enter length of z side :6
Scalene Triangle
Enter base length :2
Enter height :5
Area of Scalene Triangle 5.0
Perimeter of Scalene Triangle: 12
"""