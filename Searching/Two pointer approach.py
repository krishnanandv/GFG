
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

#Sum Pairs 
def two_pointer(arr, num):
    i=0
    n=len(arr)-1
    while(i<n):
        if((arr[i]+arr[n])==num):
            return(arr[i],arr[n])
        elif((arr[i]+arr[n])<num):
            i+=1
        else:
            n-=1
    return(-1)

print(two_pointer(arr,num))

#Find Triplet

def triplet(arr,num):
    arr.sort()
    size = len(arr)
    for i in range(0,size-2):
        #Left pointer 'l' and Right pointer 'r'
        l = i + 1
        r = size -1
        while(l<r):
            if(arr[i] + arr[l]+ arr[r] == num):
                return(arr[i] ,arr[l], arr[r])
            elif(arr[i] + arr[l]+ arr[r] < num):
                l+=1
            else:
                r-=1
    return(-1)

arr= [1, 4, 45, 6, 10, 8]
num = 22
print(triplet(arr,num))