#WRONG SOLUTION WRTITTEN
# def trap_rain(arr):
#     start = arr[0]
#     end = arr[-1]
#     level = min(arr[0],arr[-1])
#     area = level*(len(arr)-2)
#     res=0
#     for i in range(1,len(arr)-1):
#         res += arr[i]
#     total = area-res
#     if total >0:
#         return total
#     else:
#         return 0

def get_water(arr):
    lmax =[]
    rmax = [None] * len(arr)
    print(rmax)
    lmax.append(arr[0])
    for i in range(1,len(arr)):
        lmax.append(max(arr[i], lmax[i-1]))
    rmax[-1]=arr[-1]
    #print(rmax[3+1])
    for i in range(len(arr)-2,-1,-1):
        rmax[i] = (max(arr[i],rmax[i+1]))
        #print(i, arr[i], rmax[i+1])
    print(lmax)
    print(rmax)
    res =0
    for i in range(1,len(arr)-1):
        res = res +(min(lmax[i],rmax[i]) - arr[i])
    print(res)

#ar = [1,2,3]
ar = [3,0,1,2,5]
#ar = [2, 0, 2]
#ar=[3,2,1]
ar = [5,0,6,2,3]
print(get_water(ar))