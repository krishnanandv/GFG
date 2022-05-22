#This is similar to find the first occurance of an element
#Since its binary array there will be only 0s and 1s.

def find_one(arr, elem):
    n=len(arr)
    #print(elem)
    #print(n)
    low = 0
    high = n-1
    while (low <= high):
        mid = (low + high)//2
        if arr[mid] < 1:
            low = mid +1
        elif arr[mid] > 1:
            high = mid -1
        else:
            if( mid == 0 or arr[mid-1] != elem):
                return mid
            else:
                high = mid -1
    return -1

def count_ones(arr,elem):
    val = find_one(arr,elem)
    print("val",val)
    return (len(arr)-val)


arr=[0,0,0,0,0,0,0,1,1,1]
print(count_ones(arr,1))
print("---------------")
