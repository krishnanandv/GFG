li = [30, 60, 40]


def averrage_fun(arr):
    sum = 0
    for item in arr:
        sum += item
    n = len(arr)
    return sum / n


print(averrage_fun(li))