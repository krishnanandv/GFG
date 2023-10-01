#sort
# works only in list , sorts in place
l1 = [5, 10, 15, 1]
l1.sort()
print(l1)


#sorted
# works for any iterable, does not modify the passed container
l2 = [1, 5, 3, 10]
l2.sort(reverse=True)
print(l2)

l3 = ["gfg", "ide", "course"]
l3.sort()
print(l3)

# [1, 5, 10, 15]
# [10, 5, 3, 1]
# ['course', 'gfg', 'ide']