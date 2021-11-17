
def ind_ocur(arr, elem):
    for i in range(len(arr)):
        if elem == arr[i]:
            return i
    return -1

def first_occ(arr, low,high, x):
    if low > high:
        return -1
    mid = (low+high)//2
    if x>arr[mid]:
        return first_occ(arr,mid+1, high, x)
    elif x<arr[mid]:
        return first_occ(arr,low, mid-1, x)
    else:
        if (mid==0 or arr[mid-1]!=arr[mid]):
            return mid
        else:
            return first_occ(arr, low, mid-1, x)

ar = [1,1,10,10,10,20,20,40]
elem=20
#print(ind_ocur(ar,elem))
hi = len(ar)
print(first_occ(ar,0,8,10))