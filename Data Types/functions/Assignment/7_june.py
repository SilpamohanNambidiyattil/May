""" print pyramid using function ?"""
def pyramid(n):
    for i in range(1, n + 1):  # no: of rows
        for j in range(n - i):  # Spacing (blank space ddecrement)
            print('', end=' ')
        for k in range(i):  # * printing
            print('*', end=' ')
        print()
    #return
n = int(input("Enter number of levels  :"))
pyramid(n)

""" Calculator ?"""
print("_______________________________________________________")
def calculator(n1,oper,n2):
    if oper == "+":
        print(n1, "+", n2, "=", n1 + n2)
    elif oper == "-":
        print(n1, "-", n2, "=", n1 - n2)
    elif oper == "*":
        print(n1, "*", n2, "=", n1 * n2)
    elif oper == "/":
        print(n1, "/", n2, "=", n1 / n2)
    else:
        print("syntax error")
n1 = int(input())
oper = input()
n2 = int(input())
calculator(n1,oper,n2)

""" Remove repeated from list? """
print("________________________________")
def remove_dup(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
    return x
a = ["let's", "google", "the", "pineapple", "photo", "google", "photo", ""]
print("After removal :", remove_dup(a))