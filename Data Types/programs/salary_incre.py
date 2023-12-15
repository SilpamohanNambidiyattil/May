sal = int(input("enter the current salary:"))
year = int(input("enter the year of experience:"))
if (year>=5):
    sal = sal+sal*(5/100)
    print("net bouns amount:",sal)
else:
    print("not eligible for hike")