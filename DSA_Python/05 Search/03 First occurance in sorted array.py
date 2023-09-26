def focc(arr, x):

    low = 0
    high = len(arr) -1
    while (low <= high):
        mid = (low + high)//2
        print("Mid ", mid)
        if arr[mid] < x:
            low = mid +1
        elif arr[mid] > x:
            high = mid -1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid -1
    return -1
arr = [5,10,10,20,20,20,20,20,50,60,70]
print(focc(arr, 20))
arr = [5]
#print(focc(arr,10))

def f_occ_r(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    print("Mid ", mid)
    if arr[mid] < x:
        return f_occ_r(arr, x, mid + 1, high)
    elif arr[mid] > x:
        return f_occ_r(arr, x, low, mid-1)
    else:
        if (mid==0) or arr[mid-1] != arr[mid]:
            return mid
        else:
            return f_occ_r(arr, x, low, mid-1)

arr = [5,10,10,20,20,20,20,20,50,60,70]
print(f_occ_r(arr, 20, 0, len(arr)-1))
arr = [5]
print(f_occ_r(arr,100, 0, len(arr)-1))