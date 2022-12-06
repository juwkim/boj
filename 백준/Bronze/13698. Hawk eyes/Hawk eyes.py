Hawk = {'A':[1, 2], 'B':[1, 3], 'C':[1, 4], 'D':[2, 3], 'E':[2, 4], 'F':[3, 4]}
small, big = 1, 4
for change in input():
    if small in Hawk[change]:
        small = sum(Hawk[change]) - small
    if big in Hawk[change]:
        big = sum(Hawk[change]) - big
print(small, big, sep='\n')