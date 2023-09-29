
def Sroot(x):
    low = 1
    high = x
    ans = -1
    while(low <= high):
        mid = (low+high)//2
        mid_sq = mid * mid
        if mid_sq == x:
            return mid
        elif mid_sq > x:
            high = mid -1
        else:
            low = mid +1
            ans = mid
    return ans

x=9
print(Sroot(x))
