li = [1,3,4,2,5]
d1 = {x:x**3 for x in li}
print(d1)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

l3 = ['gfg','kkk','fff','ttt','fvfv']
d3 = dict(zip(li,l3))
print(d3)