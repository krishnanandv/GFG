li = [10, 41, 30, 15, 80]

def even_odd_list(arr):
    even = []
    odd = []
    for index, num in enumerate(arr):
        if index % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

even, odd = even_odd_list(li)
print("EVEN", even)
print("ODD", odd)
