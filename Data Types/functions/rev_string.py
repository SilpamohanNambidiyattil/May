"""normal program by converting string to list"""
print("Normal ")
s = 'python'
print(s)
s1 = list(s)
print(s1)
s1.reverse()
print(s1)
print(''.join(s1))


"""Using function by converting string to list"""
print("_________________________________")
print("string to list")
def reve(string1):
    s = list(string1)
    s.reverse()
    print(''.join(s))
string1='python'
reve(string1)

"""Using function by without convertng to string to list"""
print("_________________________________________")
print("withot string to list")
def rev(string):
    str1=''
    for i in string:
        str1=i+str1
    return str1
string = 'python'
print(rev(string))

"""Using list comph"""
print("_____________________________________")
print("Using list comphenssion")
stri = 'python'
st = [str[i] for i in range(len(stri)-1,-1,-1)]
print(''.join(st))