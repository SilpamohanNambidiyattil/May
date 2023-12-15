A = [1, 2, 8, 3, 4, 5]
A.sort()
print(A)
print(A[-1])


max = A[0]
for i in A :
    if i > max :
        max = i
print(max)