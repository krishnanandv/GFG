
def max_circular(arr):
    res = arr[0]
    for i in range(len(ar)):
        cur_sum = arr[i]
        cur_max = arr[i]
        for j in range(1, len(ar)):
            #print("index:", (i + j) % len(ar))
            index = (i + j) % len(ar)
            cur_sum += arr[index]
            cur_max = max(cur_max,cur_sum)
        res = max(res, cur_max)
    print(res)

#Efficient Solution
def circular_max(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        cur_sum = res + arr[0]
        res = max(res, cur_sum)
    for i in range


#ar = [3,-4,5,6,-8,7] #op -> 17
#    -1 5, 11, 3, 11

ar = [5, -2, 3, 4]
#ar = [2,3,-4]
ar = [-8,7,6]
max_circular(ar)
#
# k=5
# for j in range( len(ar)):
#     index = (k + j) % len(ar)
#     print(ar[index])

