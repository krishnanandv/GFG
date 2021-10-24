
def freq(arr):

    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] +=1
        else:
            dict[arr[i]] = 1
    print(dict)

ar = [10, 10, 10, 30 , 30 , 40]
freq(ar)


def check_freq(arr):
    dict = {}
    for elem in arr:
        if elem in dict:
            dict[elem] +=1
        else:
            dict[elem]=1
    print(dict)

check_freq(ar)





