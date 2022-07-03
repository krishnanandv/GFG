
#Naive Solution

def naive(arr, num):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if (arr[i]+arr[j] == num):
                return(arr[i],arr[j])
    return(-1)

arr = [2,5,6,8,10,20,30,40,50,65,67,78,90,99]
num=90
print(naive(arr,num))

def two_pointer(arr, num):
    i=0
    n=len(arr)-1
    while(i!=len(arr)-1):
        if((arr[i]+arr[n])==num):
            return(arr[i],arr[n])
        elif((arr[i]+arr[n])<num):
            i+=1
        else:
            n-=1
    return(-1)

print(two_pointer(arr,num))