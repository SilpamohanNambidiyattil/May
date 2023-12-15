mark = int(input("enter the mark:"))
if (mark>80):
    print("A grade")
elif (mark>=60 and mark<80):
    print("B grade")
elif (mark>=50 and mark<60):
    print("C grade")
elif (mark>=45 and mark<50):
    print("D grade")
elif (mark>=25 and mark<45):
    print("E grade")
elif (mark<25):
    print("F grade")
else:
    print("no graded")