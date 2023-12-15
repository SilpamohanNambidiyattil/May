""" 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit? """

temperature = float(input('Enter temperature :'))
print('Given Temperature :',temperature)
if temperature >= 0:
     f = (temperature*(9/5))+32
     print('Degree Celsius to Fahrenheit :',f)
     c = (temperature-32)*(5/9)
     print('Fahrenheit to Degree Celsius :',c)
"""
OUTPUT
Enter temperature :3
Given Temperature : 3.0
Degree Celsius to Fahrenheit : 37.4
Fahrenheit to Degree Celsius : -16.11111111111111
"""