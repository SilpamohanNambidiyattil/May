"""return"""
#def sum ():
    #a=6
    #b=7
    #c=a+b
    #print(c)
#sum()

#def sum1(a,b):
    #c=a+b
    #return c # returns c , c contains a+b
#print(sum1(5,6))

"""sum of n natural numbers using function"""
def sum_natural(num): # pass num as parameter to the function
    sum = 0
    for i in range(num+1): # range num+1
        sum = sum+i
    return sum # return sum
num = int(input("Enter the number limit :"))
print("sum of natural numbers :", sum_natural(num)) #sum_natural function is called with num as argument


