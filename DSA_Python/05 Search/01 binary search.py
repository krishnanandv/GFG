def bsearch(arr, x):

    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr = [10,20,30,40,50,60,90,110,150,170,1645]
print(bsearch(arr,110))
print(bsearch(arr,1110))
