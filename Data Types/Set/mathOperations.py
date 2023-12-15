A = {"priya",12,"python","btech"}
B = {"silpa",12,"python","mtech","python"}
print(A)
print(B)
print(A.union(B))
#print(A.difference(B))
#print(A.intersection(B))
print(A.symmetric_difference(B))

x = A.difference_update(B)
print(A)
y = A.intersection_update(B)
print(A)
z = A.symmetric_difference_update(B)
print(A)

