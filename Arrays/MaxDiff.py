
def max_diff(arr):

    minval = arr[0]
    res = arr[1] - arr[0]
    for i in range(1,len(arr)):
        res = max(res, arr[i]-minval)
        minval = min(minval, arr[i])
    print(res)

ar = [10,2,3,10,6,4,8,1]
max_diff(ar)



def check_max(arr):
    large_diff = arr[1]-arr[0]
    min_elem=arr[0]
    for i in range(1,len(arr)):
            large_diff = max(large_diff, arr[i]-min_elem)
            min_elem = min(min_elem, arr[i])
    print(large_diff)

check_max(ar)





