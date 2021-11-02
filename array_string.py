#Remove duplicates from sorted array Constant extra space

NO_OF_CHARS =256

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


#Count pairs with given sum

def pair_sum(arr,sum):
    diff_map ={}
    count = 0
    for x in arr:
        if sum - x in diff_map:
            diff_map[sum - x] = diff_map[sum - x] + 1
        else:
            diff_map[sum - x] = 1

    for x in arr:
            count += diff_map[x]

    return count /2



#sort array in wave form

def wave_arr(arr):

    for i in range(0,len(arr)-1):
        if i % 2 ==0:
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        if i % 2 ==1:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

    return arr


#intersection of sorted arrs

def intersect_arrs(arr1,arr2):
    len1=len(arr1)
    len2=len(arr2)
    intersect = []
    i=0
    j=0

    while i<len1 and j<len2:
        if arr1[i]<arr2[j]:
            i+=1
        if arr1[i]>arr2[j]:
            j+=1
        else:
            intersect.append(arr1[i])
            i+=1
            j+=1
    return set(intersect)


#majority element in array

def majority_element(arr):
    maj_candidate=arr[0]
    counter = 1
    for i in range(1,len(arr)):
        if arr[i]==maj_candidate:
            counter+=1
        else:
            counter-=1
        if counter == 0:
                maj_candidate =arr[i]
                counter =1

    if is_majority(arr,maj_candidate):
        return maj_candidate

    return None

def is_majority(arr, cand):
    count = 0
    for i in range(len(arr)):
        if arr[i] == cand:
            count += 1
    if count > len(arr)/2:
        return True
    else:
        return False



#find min distance

def find_min_distance(arr,x,y):
    min_dist = 10000000000000000000
    previous_number= x
    previous_index=0
    dist = 0
    for i in range(0,len(arr)):
        if (arr[i] == x or arr[i] == y) and arr[i] != previous_number:
            dist=i - previous_index
            if dist<min_dist:
                min_dist=dist
            previous_number = arr[i]
            previous_index = i


    return min_dist



#Find subarray with given sum

def sub_sum(arr,desired_sum):
    sub_sum = 0
    start_index = 0
    for i in range(0, len(arr)):
        sub_sum = sub_sum + arr[i]

        if sub_sum == desired_sum:
            print(f'{start_index} to {i}')
            sub_sum = 0
            start_index = i

        if sub_sum > desired_sum:
            sub_sum = sub_sum - arr[start_index]
            start_index += 1




#Adding one to number represented as array of digits

def add_one(arr):
    arr_len =len(arr)-1
    carry = 0
    arr[arr_len]=arr[arr_len]+1
    if arr[arr_len]==10:
        arr[arr_len] = 0
        carry =1


    for i in range(arr_len-1,-1,-1):
            if carry ==1:
                arr[i] += 1
                if arr[i] == 10:
                    arr[i] = 0
                    if i == 0:
                        arr.insert(0, 1)

    return arr


def anagrams(arr1,arr2):
    if len(arr1)!=len(arr2):
        return False
    arr1_tmp= [0] * NO_OF_CHARS
    arr2_tmp = [0] * NO_OF_CHARS

    for x in arr1:
        m = ord(x)
        arr1_tmp[m] = 1

    for x in arr2:
        m = ord(x)
        arr2_tmp[m] = 1

    for i in range(0,NO_OF_CHARS):
        if arr1_tmp[i] != arr2_tmp[i]:
            return 0



def max_diff(arr):
    min_num = 100000000000
    diff = 0

    for i in range(0,len(arr)-1):
        if arr[i] < min_num :
            min_num = arr[i]
        curr_diff = arr[i]-min_num
        if curr_diff > diff:
            diff = curr_diff

    return diff


def subbaray_sum(arr,sum_desired):
    cur_sum = 0
    left = 0
    for i in range(0, len(arr)):
        cur_sum = cur_sum + arr[i]

        if cur_sum > sum_desired:
            while cur_sum > sum_desired:
                cur_sum  = cur_sum - arr[left]
                left += 1

        if cur_sum == sum_desired:
            print(f"index {left-1} to {i} ")
            return True

arr =[1, 4, 20, 3, 10, 5]
sum = 33





arr1 = [1, 4, 20, 3, 10, 5]


print("Count of pairs is", subbaray_sum(arr1,33))