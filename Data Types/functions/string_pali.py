def rev(string):
    str1=''
    for i in string:
        str1=i+str1
    return str1
string = input("Enter your string :")
if rev(string)==string: # add this if condition inside function then call the function is also correct
    print(string,"is paliendrome")
else :
    print(string,"is not paliendrome")

"""using list"""
def pali(string):
    string=[string[i] for i in range(len(string)-1,-1,-1)]
    print(string)
    x=''.join(string)
    if x==s:
        print("pali")
    else:
        print("not pali")
    return x
s=input("enter string :")
pali(s)