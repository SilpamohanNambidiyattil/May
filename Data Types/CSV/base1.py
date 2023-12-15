import csv
with open('sample.csv', 'r', newline='\n') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open('sample.csv','w')as file:
    writer = csv.writer(file)
    writer.writerow(['Series_reference','Period','Data_value'])
    writer.writerow(['BDCQ.SEA1AA','2011.06','80078'])
    file.close()

with open('test.csv','w',newline='\n')as fcsv:
    fieldnames = ["First_name","Last_name","Age","Year"]
    writer = csv.DictWriter(fcsv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"First_name":"silpamohan","Last_name":"n","Age":25,"Year":1997})
    writer.writerow({"First_name": "akshaymohan", "Last_name": "n", "Age": 26, "Year": 1996})
    fcsv.close()
with open('test.csv', 'r') as fcsv:
    reader = csv.DictReader(fcsv)
    for row in reader:
        print(row)
