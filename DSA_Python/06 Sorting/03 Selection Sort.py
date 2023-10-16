
def selection_sort(arr):

    min_ind = 0
    n = len(arr)
    for i in range(n-1):
        #print(i,arr[i])
        min_ind = i
        for j in range(i+1,n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    return (arr)


arr = [10,5,8,20,2,18]

print(selection_sort(arr))



