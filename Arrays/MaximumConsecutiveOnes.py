# Input takes only binary array
# Find Maximum consecutive ones
def maxOnes(arr):
    count = 0
    curr_count = 0
    allOnes = True
    for i in range(len(arr)):
        if arr[i]==1:
            curr_count += 1
        else:
            allOnes = False
            if curr_count>=count:
                count = curr_count
            curr_count=0
    if(allOnes):
        count = curr_count
    print(count, "Maximum Consecutive Ones")

ar = [1,1,1,1]
ar = [0,1,1,0,1,0]
ar = [0,0,0]
maxOnes(ar)