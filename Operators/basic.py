#OPERATORS
#ARITHEMATIC

print("arithematic")
a=5
b=2
sum=a+b
print(sum)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)

# Assignment Operators
print("assignment")
x=5
#x=x+3
#print(x)

#x+=3
x*=3
print(x)

#comparison
print("comparison")
x=5
y=7
print(x==y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x!=y)

print("**logical**")
a= x>y and y<x
print(a) # 5>7-> no(false)  and 7<5-> no(false) then it returns false
print(x<y or x>y)
print(not(x>3 and x<10)) # 5>3 and 5<10 (true) then not it (false)
print("** concatinaging **")
x="python "
y=" is"
z= " awesome"
print(x+y+z)
