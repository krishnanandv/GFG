
def binary_rec(arr, elem, left, right):
    mid = (left + right)//2
    if left>right:
        return -1
    if arr[mid] == elem:
        return mid
    elif elem > arr[mid]:
        return binary_rec(arr,elem, mid+1, right)
    elif elem < arr[mid]:
        return binary_rec(arr, elem, left, mid-1)
    else:
        return -1

arr = [10,20,30,40,50,60]
elem = 20
aa = binary_rec(arr, elem,0,len(arr)-1)
print(aa)

arr = [10,20,30,40]
elem = 13
bb = binary_rec(arr, elem,0,len(arr)-1)
print(bb)