def loccr(arr, x):
    low =0
    high = len(arr)-1
    while(low <= high):
        mid = (low + high) // 2
        print("Mid", mid)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
        else:
            if (mid==len(arr)-1) or (arr[mid]!=arr[mid+1]):
                return mid
            else:
                low = mid + 1
    return -1

arr = [5,10,10,20,20,20,20,20,50,60,70]
print(loccr(arr, 20))
arr = [5]
print(loccr(arr,10))