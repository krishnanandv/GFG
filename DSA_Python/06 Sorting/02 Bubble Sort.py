def Bubble_sort(arr):

    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [2,7,6,10,8]
print(Bubble_sort(arr))

#Time Complexity - O(n2)

def Otimized_BS(arr):
    n=len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped==False:
            return

arr = [2,7,6,10,8]
Otimized_BS(arr)
print(arr)
