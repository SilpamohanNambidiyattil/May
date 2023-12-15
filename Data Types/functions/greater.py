def largest(n1,n2,n3):
    if (n1 >= n2) and (n1 >= n3):
        return n1
    elif (n2 >= n1) and (n2 >= n3):
        return n2
    else:
        return n3

n1 = int(input("Enter number_1:"))
n2 = int(input("Enter number_2:"))
n3 = int(input("Enter number_3:"))
print("Largest among three numbers :", largest(n1,n2,n3))

