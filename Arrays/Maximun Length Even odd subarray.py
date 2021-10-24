
def max_leng(arr):
    cur_count = 1
    res = 1
    for i in range(1,len(arr)):
        if (arr[i]%2==0 and arr[i-1]%2==1) or (arr[i]%2!=0 and arr[i-1]%2==0):
            cur_count+=1
            res = max(res, cur_count)
        else:
            cur_count=1
    #final = max(res, cur_count)
    print(res)

#ar = [10,12,14,7,8]
ar = [1,1,1,1]
ar = [7,10,13,14]
ar= [10,12,8,4,1,2,3,4,4,4,4,5,6,7,8,9]
#ar=[1]
max_leng(ar)