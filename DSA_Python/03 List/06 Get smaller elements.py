li = [8, 100, 20, 40, 3, 7]
input = 10

li2 = [100,20,40,60,80,200]
inp2 = 60
def get_smaller_elements(arr, input):
    smaller_list = []
    for elem in arr:
        if elem < input:
            smaller_list.append(elem)
    return smaller_list

print(get_smaller_elements(li,input))
print(get_smaller_elements(li2,inp2))