
def MissingNumber(array, n):
    # code here
    total = (n * (n + 1)) / 2
    array_sum = sum(array)
    missing = int(total - array_sum)
    print(missing)


ar = [1,2,3,5]
l = 5
ar = [6,1,2,8,3,4,7,10,5]
l=10
MissingNumber(ar, l)