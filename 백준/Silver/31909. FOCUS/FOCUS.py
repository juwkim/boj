N = int(input())
pos = [*range(8)]
for num in map(int, input().split()):
    b = bin(num)[2:]
    if b.count('1') == 2:
        i = len(b) - 1 - b.index('1')
        j = len(b) - 1 - b.rindex('1')
        pos[i], pos[j] = pos[j], pos[i]
print(pos[int(input())])