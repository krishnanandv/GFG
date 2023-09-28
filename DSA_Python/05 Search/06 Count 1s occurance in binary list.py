def one_occr(arr):
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low + high)//2
        if arr[mid] < 1:
            low = mid +1
        elif arr[mid] >1:
            high = mid -1
        else:
            if mid==0 or (arr[mid-1]!=arr[mid]):
                return mid
            else:
                high = mid -1
    return -1


arr = [0,0,0,0,1,1,1,1]
occur = one_occr(arr)
if occur!=-1:
    print("Count of 1's:", len(arr)-occur)
else:
    print("None")
