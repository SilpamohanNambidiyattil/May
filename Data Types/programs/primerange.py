prime = []
for i in range(0, 51):
    flag = 0
    if i == 0 or i==1:
        continue
    else:
        for j in range(2,i):
            if i%j ==0:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
                prime.append(i)
print(prime)