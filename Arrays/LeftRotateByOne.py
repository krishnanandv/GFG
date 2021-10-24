
def leftRot(arr):

    temp = arr[0]
    for i in range(0,len(arr)-1):
        arr[i]=arr[i+1]
    #print(arr)
    #print(i)
    arr[i+1] = temp
    print(arr)

ar = [2,3,4,5,7,8,9,0,0,8,78]
leftRot(ar)