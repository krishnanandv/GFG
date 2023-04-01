def check_sort(arr):
    if len(arr)<=1:
        return True
    point = arr[0]
    for elem in arr[1:]:
        if elem < point:
            return False
        else:
            point = elem
    return True

arr=[1]
print(check_sort(arr))

arr=[2,3,4,5]
print(check_sort(arr))

arr = [3,4,1]
print(check_sort(arr))