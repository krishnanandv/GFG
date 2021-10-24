
def leftRotD(arr, d):
    print(arr)
    temp = []
    for i in range(0,d):
        temp.append(arr[i])
    print(temp)
    for i in range(d,len(arr)):
        arr[i-d] =arr[i]
    print(arr)
    n = len(arr)
    for i in range(0, len(temp)):
        arr[n-d+i] = temp[i]

    print(arr)


def lefR(arr, d):
    reverse(arr, 0, d-1)
    reverse(arr, d, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    print(arr)
def reverse(arr, low, high):
    while(low<high):
        arr[low],arr[high] = arr[high],arr[low]
        low +=1
        high -=1




ar = [1,2,3,4,5,6,7]
d=2
lefR(ar,d)

