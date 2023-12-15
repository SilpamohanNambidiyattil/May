def search(items,n,key):
    for i in range(0,n):
        if (items[i]==key):
            return i
    return -1
items=[2,3,1,4,5,7,8,10,20,30]
key=20
n=len(items)
result = search(items,n,key)
if result==-1:
    print("item not present ")
else:
    print("item is present at index ",result)
