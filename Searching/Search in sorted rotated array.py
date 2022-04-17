#Given array is sorted rotated array and once we take the mif of array alway one of the half
#of array will be sorted.
def searchRotArr(arr, elem):
    n=len(arr)
    low= 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]==elem:
            return mid
        ##If Left half is sorted
        elif arr[low]<arr[mid]:
            if(elem>=arr[low] and elem<arr[mid]):
                high = mid-1
            else:
                low = mid+1
        ##If right half is sorted
        else:
            if (elem>arr[mid] and elem <= arr[high]):
                low = mid+1
            else:
                high = mid -1
    return -1

arr = [10,20,40,60,5,7,8,9]
print(searchRotArr(arr,7))