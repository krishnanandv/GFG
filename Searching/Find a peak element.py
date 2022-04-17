#1)navie solution - Given a unsorted array and find the peak
def naivePeak(arr):
    n=len(arr)
    #print(n)
    if n==0:
        return -1
    elif arr[0]>arr[1]:
        return arr[0]
    elif arr[n-1]>arr[n-2]:
        return arr[n-1]
    for i in range(1,n-1):
        if (arr[i]>arr[i-1] and arr[i]>arr[i+1]):
            return arr[i]
#arr=[1,20]
#arr=[1,20,24,11,9,17,21,55,1,2,0]
#print(naivePeak(arr))

#Efficient solution
def FindPeak(arr):
    n=len(arr)
    #print(n)
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if ((mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or (arr[mid+1]<=arr[mid]))):
            return arr[mid]
        elif (mid>0 and arr[mid-1]>=arr[mid]):
            high = mid-1
        else:
            low = mid+1
    return -1

arr=[1,20]
print(FindPeak(arr))