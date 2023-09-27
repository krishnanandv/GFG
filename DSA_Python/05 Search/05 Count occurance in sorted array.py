def Foccur(arr, x):
    low = 0
    high = len(arr)-1
    while (low<=high):
        mid = (low + high)//2
        print("Mid ", mid)
        if arr[mid] < x:
            low = mid +1
        elif arr[mid] > x:
            high = mid -1
        else:
            if (mid==0 or (arr[mid-1] != arr[mid])):
                return mid
            else:
                high = mid -1
    return -1

def Loccur(arr, x):
    low = 0
    high = len(arr)-1
    while (low<=high):
        mid = (low + high)//2
        print("Mid ", mid)
        if arr[mid] < x:
            low = mid +1
        elif arr[mid] > x:
            high = mid -1
        else:
            if (mid==len(arr)-1 or (arr[mid] != arr[mid+1])):
                return mid
            else:
                low = mid +1
    return -1

def coour(arr, x):
    first = Foccur(arr, x)
    last = Loccur(arr, x)
    if first==-1:
        return 0
    else:
        return(last-first+1)

arr = [5,10,10,20,20,20,20,20,50,60,70]
#arr = [20,20]

print("Count = ", coour(arr, 20))

