def binary(items,l,r,key):
    while l<=r:
        mid = l+(r-1)//2
        if items[mid]==key:
            return mid
        elif items[mid]<key:
            l=mid+1
        else:
            r=mid-1
    return -1
items=[2,3,1,4,5,7,8,10,20,30]
key=20
result = binary(items,0,len(items)-1,key)
if result!=-1:
    print("item is present at index ",result)
else:
    print("item not present" )
