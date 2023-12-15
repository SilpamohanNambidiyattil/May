"""Print the given String in the specified format in a single  line of code
Twinkle, twinkle, little star,
    How I wounder what you are !
        Up above the world so high,
        Like a diamond in the sky."""
print("Twinkle, twinkle, little star, \n\tHow I wounder what you are ! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.")

""" Program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers."""
#values = input("Input some comma seprated numbers : ")
#list = values.split(",")
#tuple = tuple(list)
#print('List : ',list)
#print('Tuple : ',tuple)



list1 =[1,2,3,4,5,6,7,8,9]
#temp =0
prime = [i for i in list1 if 0 not in [ i%j for j in range(2,i//2)]]
#prime = [i for i in list1  (i%j) for j in range(2,i//2) if i%j!=0]
print("prime number from the list:",prime)

n = int(input("enter the limit :"))
ex = [i for i in range(n) if i!=3 or  i!=5 continue ]
print(ex)