

def moveZ(arr):
    # [8, 5, 0,0, 10, 0, 20]
    count = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i], arr[count] = arr[count], arr[i]
            count +=1
    print(arr)

moveZ([8, 5, 0,0, 10, 0, 20])