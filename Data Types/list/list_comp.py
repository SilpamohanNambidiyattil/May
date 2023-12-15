""" Odd and Even list """
list1 =[1,2,3,4,5,6,7,8,9]
even = [i for  i in list1 if i%2==0]
print("even",even)
odd = [j for j in list1 if j%2!=0]
print("odd",odd)

""" print string inculding 'a' only """
list2 =["apple","orange","banana","kiwi","grapes"]
a_list = [i for i in list2 if 'a' in i]
print(a_list)
b_list = [j for j in list2 if 'a' not in j]
print(b_list)

"""print prime numbers from a list """
prime = [i for i in list1 if 0 not in [ i%j for j in range(2,i)] ]

prime2 = [i for i in list1 if all (i % j != 0 for j in range(2, i))]
print("prime number from the list_way 1:",prime)
print("prime number from the list_way 2:",prime2)

""" print numbers except 3 and 5 from a range """
n = int(input("enter the limit :"))
ex = [i for i in range(n) if i!=3 if i!=5 ]
print(ex)

""" print negative and positive numbers from a list """
A = [1, 7, -8, 6, -5, 2, -4, 0,0]
pos = [i for i in A if i>0]
print("Positive list :", pos)
neg = [i for i in A if i <0]
print("Negative list :", neg)
zero = [i for i in A if i==0]
print("zero list:", zero)

""" Program to remove vowels from a string """
s = input("Enter the String :")
x = list(s)
print(s)
new_x = [i for i in x if i not in 'AEIOUaeiou']
print(new_x)
y = ''.join(new_x)
print("vowels removed String :",y)


s1 = input("Enter the String :")
words = list(s1)
new_s = [word for word in words if len(word)<5 ]
print(new_s)
