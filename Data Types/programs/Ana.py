"""vowel """
x = input("Enter a character :")
#str1 = ("a","e","i","o","u")
if x=='a' or x=='e' or x=='i'or x=='o' or x=='u':
    print("character is vowel")
else:
    print("Character is consonant")


str1 = input("enter a string :")
print('Vowels: ')
for i in str1:
   if i in "AEIOUaeiou":
      print(i, end=' ')

print('\nConsonants: ')
for i in str1:
   if i not in "AEIOUaeiou ":
      print(i, end=' ')

s = input("enter string :")
i=0
sn=[]
while i < len(s):
    if s[i]=="e" or s[i]=="o" :
        i = i+1
        break
    print(sn.append(i))