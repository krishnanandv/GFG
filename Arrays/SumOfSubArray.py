#Sum on continues element for a given array - having highest sum
# Naive Solution O(n2)

def naive_sub(arr):
    result = arr[0]
    for i in range(len(arr)):
        curr = 0
        for j in range(i,len(arr)):
            curr = curr+ arr[j]
            result = max(result, curr)
    print("Maximum Sum of sub array:", result)

# Efficient Solution O(n)
def max_subArray(arr):
    max_sum = arr[0]
    for i in range(1,len(arr)):
        cur_sum = max_sum + arr[i]
        max_sum = max(cur_sum, arr[i])
    print("Maximum Sum of sub array:", max_sum)

ar = [1,-2,3,-1,2]
#naive_sub(ar)
max_subArray(ar)