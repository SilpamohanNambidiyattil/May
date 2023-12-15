"""Given a sentence , reverse each word but don't reverse the sentence?"""
str1 = input("Enter a string :")
x=str1.split()
print(x)
rev =[]
for i in x:
    rev.append(i[::-1])
    #print(rev)
    new_rev= " ".join(rev)
    #print(new_rev)
print(new_rev)


