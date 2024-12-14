l, r = 0, 1e9
for num in map(int, [*open(0)][1].split()):
    l, r = num - min(num, r), num - l
print(max(0, r - l + 1))