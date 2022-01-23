def last_occur(arr, x):
    low = 0
    high = len(arr)-1
    while(low <= high):
        mid = (low + high)//2
        if(arr[mid] > x):
            high = mid -1
        elif(arr[mid] < x):
            low = mid +1
        else:
            if (mid==len(arr)-1 or arr[mid+1]!=arr[mid]):
                return mid
            else:
                low = mid +1

arr = [10,15,20, 20, 40, 40]
x =40
print(last_occur(arr, x))