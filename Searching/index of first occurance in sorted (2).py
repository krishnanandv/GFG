#Naive Solution
# Display the firat occurance of the number in the given sorted array
# If element not present then return -1

def naive_find_first_occur(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return(i)
    return (-1)

def first_occur(arr,low,high,x):
    if low > high:
        return -1
    mid = (low+high)//2
    if x>arr[mid]:
        return first_occur()
    return(-1)




#Test Case - Naive Solution
# arr = [1,10,10,20,30,40,50,100]
# x=40
# print(naive_find_first_occur(arr,x))
# arr = [10,20,30]
# x=15
# print(naive_find_first_occur(arr,x))

#Solution
arr = [1,10,10,20,30,40,50,100]
x=40
print(first_occur(arr,x))
# arr = [10,20,30]
# x=15
# print(first_occur(arr,x))

