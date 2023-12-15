dict = {5:2,6:4,7:3,8:1,9:0}
val = list(dict.items())
print(val)

newval = []
newvalf=[]
for i in val:
    irev=i[::-1]
    newval.append(irev)
print(newval)
#val.clear()
newval.sort()
print(newval)

for i in newval:
    irevf=i[::-1]
    newvalf.append(irevf)
print(newvalf)

dec = newvalf[::-1]
print(dec)

""" unic"""
#dict1 = {"v":"s001","b":"s001","n":"s002"}
#set_val=set()
#for i in dict1:
    #for j in i.values():
        #set_val.add(j)
#print(set_val)

def count(arr,n):
    visited = [False for i in range(n)] # mark all arr elements are not visited
    for i in range(n):# traverse through all elements and count frequency
        if visited[i]==True:# skip element already processed
            continue
        count =1#count frequency
        for j in range(i+1,n,1):# iterate loop i+1 to n
            if (arr[i]==arr[j]):
                visited[j]=True
                count+=1
        if count==1:
            print(arr[i])
dict1 = {"v":"s001","b":"s001","n":"s002"}
arr1 = dict1.values()
arr=list(arr1)
print(arr)
n=len(arr)
count(arr,n)