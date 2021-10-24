
def stock(arr, start, end):
    if (end <= start):
        return 0
    max_profit =0
    for i in range(start,end,1):
        for j in range(i+1, end+1):
            if arr[j]>arr[i]:
                #curr_profit = arr[j]-arr[i] + max_profit(arr,start,i-1) + max_profit(arr,j+1,end)
                curr_profit = arr[j] - arr[i] +\
                            stock(arr, start, i - 1)+ \
                            stock(arr, j + 1, end);
                max_profit = max(max_profit, curr_profit);
    return max_profit


ar =[1,5,3,8,12]

#price = [1,5,3,8,12]
# ar = [30, 20, 10]
# ar = [1,5,3,1,2,8]
# ar = [100, 180, 260, 310, 40, 535, 695]
e = len(ar)-1
print(stock(ar,0,e))
