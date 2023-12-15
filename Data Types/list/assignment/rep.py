a = ["let's google the pineapple" ]
print("Given list:", a)
b = "".join(a)
print(b)

t = " "
for i in b:
    if i in t :
        continue
    else :
        t = t+i
    #print(t)


print("duplicates removed list:", t)
x = list(t)
print(x)