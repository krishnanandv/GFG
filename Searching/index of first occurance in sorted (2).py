#Naive Solution
# Display the first occurance of the number in the given sorted array
# If element not present then return -1

def naive_find_first_occur(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return(i)
    return (-1)

#Recursive Call
def first_occur(arr,low,high,x):
    if low > high:
        return -1
    mid = (low+high)//2
    if x > arr[mid]:
        return first_occur(arr,mid+1,high,x)
    elif x < arr[mid]:
        return first_occur(arr,low, mid-1, x)
    else:
        if (mid==0 or arr[mid-1]!=arr[mid]):
            return mid
        else:
            first_occur(arr,low,mid-1,x)

# Iterative Call
def itr_first_occur(arr, x):
    low = 0
    high = len(arr)-1
    while(low <= high):
        mid = (low + high)//2
        if arr[mid] > x:
            high = mid -1
        elif arr[mid] < x:
            low = mid+1
        else:
            if (mid==0 or arr[mid-1]!=arr[mid]):
                return mid
            else:
                high = mid-1
    return -1


#Test Case - Naive Solution
# arr = [1,10,10,20,30,40,50,100]
# x=40
# print(naive_find_first_occur(arr,x))
# arr = [10,20,30]
# x=15
# print(naive_find_first_occur(arr,x))

#Solution
# arr = [1,10,10,20,30,40,50,100]
# x=40
# print(first_occur(arr,0, 7,x))
# #Test 2
# arr = [10,20,30]
# x=15
# print(first_occur(arr,0,2,x))
# #Test 3
# arr=[4,5]
# x=4
# print(first_occur(arr,0,1,x))

#Test Iterative Solution
arr = [5,5,5]
x=5
print(itr_first_occur(arr,x))
# Test 2
arr = [5,10,10,20,20]
x=20
print(itr_first_occur(arr,x))