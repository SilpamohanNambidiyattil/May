person_count = 100
a = []
for i in range(1,person_count+1):
    #a = i + 1
    a.append(i)
#print(a,end=' ')

for i in a:
    if (i%2==0):
        a.remove(i)
print(a)