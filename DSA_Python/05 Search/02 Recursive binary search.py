def Rbinary(arr,x, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return Rbinary(arr, x, mid+1, high)
    else:
        return Rbinary(arr, x, low, mid -1)

arr = [10,20,30,40,50,60,90,110,150,170,1645]
print(Rbinary(arr,110, 0, len(arr)-1))
print(Rbinary(arr,1110, 0, len(arr)-1))