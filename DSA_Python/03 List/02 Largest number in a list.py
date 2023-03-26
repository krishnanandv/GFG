def large_num(arr):
    if not arr:
        return None
    large = arr[0]
    if len(arr) > 1 :
        for elem in arr:
            if elem > large:
                large = elem
    return large


arr = [4, 5, 3, 2, 11]
print(large_num(arr))

arr = [40]
print(large_num(arr))

arr = [30, 30, 30]
print(large_num(arr))

arr = []
print(large_num(arr))