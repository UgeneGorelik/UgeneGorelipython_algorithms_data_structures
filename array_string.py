#Remove duplicates from sorted array Constant extra space

def remove_duplicates_constant(arr):
    j = 0
    for i in range(0,len(arr)-1):
        if arr[i]!=arr[i+1]:
           arr[j]=arr[i]
           j+=1
    arr[j] = arr[len(arr)-1]
    return arr[:j+1]


#merge two sorted arrays

def merge_arrays(arr1,arr2):
    len1=len(arr1)
    len2=len(arr2)
    result_array=[None]*(len1+len2-1)
    j=0
    i=0
    k=0
    while (i<len1 and j<len2):
        if arr1[i]<arr2[j]:
           result_array[k]=arr1[i]
           i+=1
           k+=1
        else:
            result_array[k]=arr2[j]
            j += 1
            k += 1
    if len(arr1[i:])>0:
        result_array.extend(arr1[i:])
    if len(arr1[j:]) > 0:
        result_array.extend(arr2[j:])

    return result_array




#zig zag array
def zig_zag(arr):
    flag = True

    for i in range(0,len(arr)-1):
        if flag:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

        else:
            arr[i] < arr[i+1]
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        flag = not flag

    return arr




arr=[3,4,6,2,1,8,9]
print(zig_zag(arr))