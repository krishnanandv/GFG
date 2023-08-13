
arr = [10,10,20,20,20,30,40,40,40,40,40]
arr2 = [10]
def rem_dup(arr):
    if len(arr)==0:
        return None
    if len(arr)==1:
        return arr
    pos = 1
    cur = arr[0]
    for i in range(1,len(arr)):
        if(arr[pos-1] != arr[i]):
            arr[pos] = arr[i]
            pos +=1
    return (arr,pos)


print(rem_dup(arr))