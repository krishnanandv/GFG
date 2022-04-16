#This code will return if perfect square root exists or else it will return floor of
#nearest square root

def sqroot(val):
    low =1
    high = val
    ans =0
    while(low<=high):
        mid = (low +high)//2
        if (mid*mid < val):
            low = mid+1
            ans = mid
        elif (mid*mid >val):
            high = mid-1
        else:
            return (mid)
    return(ans)

print(sqroot(99))
        