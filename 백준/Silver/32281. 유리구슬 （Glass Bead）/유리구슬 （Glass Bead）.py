input()
print(sum(l * (l + 1) for l in map(len, input().split('0'))) >> 1)