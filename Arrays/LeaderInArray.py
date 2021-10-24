
def leader(arr):
    elem = arr[-1]
    temp = [elem]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] >elem:
            temp.append(arr[i])
            elem = arr[i]
    print(temp)

ar = [77,7, 10, 4, 10, 6, 5, 2]
leader(ar)
