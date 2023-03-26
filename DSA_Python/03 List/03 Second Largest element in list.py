def second_large(arr):
    if len(arr) <= 1:
        return None
    large = arr[0]
    s_large = None
    for elem in arr[1:]:
        if elem > large:
            s_large = large
            large = elem
        elif elem != large:
            if s_large == None or s_large < elem:
                s_large = elem
    return s_large

arr = [55, 4, 5, 3, 2, 11]
print(second_large(arr))

arr = [40]
print(second_large(arr))

arr = [30, 30, 30]
print(second_large(arr))

arr = []
print(second_large(arr))
            