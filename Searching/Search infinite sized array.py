#Time complexity is O(log(position))

def infiSearch(arr, elem):
    if arr[0]==elem:
        return 0
    i=1
    now=-1
    #Making i's value double in every itreation
    #Once array[i] crosses the element which we want to find and not found yet
    #Will move to do a binary search from the last position of i to (i*2)
    while(arr[i]<=elem):
        if arr[i]==elem:
            return i
        else:
            now=i
            i = i *2
    #Doing a binary search
    while(now<=i):
        mid = (now+i)//2
        if (arr[mid]<elem):
            now = mid+1
        elif(arr[mid]>elem):
            i = mid-1
        else:
            return mid
    return -1

arr= list(range(0,10000,5))
#print(arr)
print(infiSearch(arr,17))


