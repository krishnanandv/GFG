
def naive_maj(arr):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] +=1
        else:
            dict[arr[i]] = 1

    m = len(arr)/2
    elem = max(dict)
    print("max", elem)
    if dict[elem] > m:
        for i in range(len(arr)):
            if arr[i] == elem:
                print(i)
    else:
        print(-1)
ar = [8,3,4,8,8]
ar = [3,7,4,7,7,5]
naive_maj(ar)