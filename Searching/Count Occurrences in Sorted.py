def firstocc(arr, elem):
    n = len(arr)
    low =0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]<elem:
            low = mid+1
        elif arr[mid]>elem:
            high=mid-1
        else:
            if (mid==0 or arr[mid-1]!=elem):
                return mid
            else:
                high = mid-1
    return -1
def lastocc(arr, elem):
    n = len(arr)
    low =0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] < elem :
            low = mid+1
        elif arr[mid] > elem:
            high = mid-1
        else:
            if(mid==n-1 or arr[mid+1]!=elem):
                return mid
            else:
                low = mid+1
    return -1

def count_of_occur(arr,elem):
    first = firstocc(arr,elem)
    if first==-1:
        return 0
    else:
        return (lastocc(arr,elem) - first +1)

arr = [-1,-1,-1,0,0,0,0,0,0,0,12,15,17,19,20,20,20,50]
#arr = [50,50,50,50,45,45,43,37,15,15,15]
print(count_of_occur(arr,20))