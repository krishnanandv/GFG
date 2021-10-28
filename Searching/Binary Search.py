
def binary_search(arr, x):
    mid = -1
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            low = mid +1
        else:
            high = mid -1
    return (mid)

ar = [10,20,30,40,50,60]
print(binary_search(ar, 20))