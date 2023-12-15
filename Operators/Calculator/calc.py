n1 = int(input())
oper = input()
n2 = int(input())
if oper == "+":
    print(n1, "+", n2, "=", n1+n2)
elif oper == "-":
    print(n1, "-", n2, "=", n1 - n2)
elif oper == "*":
    print(n1, "*", n2, "=", n1 * n2)
elif oper == "/":
    print(n1, "/", n2, "=", n1 / n2)
else:
    print("syntax error")