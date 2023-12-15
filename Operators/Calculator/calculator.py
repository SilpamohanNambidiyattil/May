n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
print("available operations are: +,-,*,/")
select = input("select operation:")
if select == "+" :
    print(n1, "+", n2, "=",n1+n2)
elif select == "-" :
    print(n1, "-", n2, "=", n1 - n2)
elif select == "*" :
    print(n1, "*", n2, "=", n1 * n2)
elif select == "/" :
    print(n1, "/", n2, "=", n1 / n2)
else :
    print("syntax error")