""" Train """

def finfPlatform(arr,dep,len_arr):
    #platform = 1
    result = 1
    for i in range(len_arr):
        platform = 1
        for j in range(len_arr):
            if (i != j) :
                if (arr[i]>=arr[j] and (dep[j]>=arr[i])):
                    platform = platform+1
        result = max(result, platform)
    return result
arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]
len_arr = len(arr)
print("No: platform :", finfPlatform(arr,dep,len_arr))