

def maxprofit(arr):
    profit = 0

    for i in range(1, len(arr)):
        if (arr[i]>arr[i-1]):
            profit = profit + arr[i]-arr[i-1]
    print(profit)

ar =[1,5,3,8,12]
maxprofit(ar)