n, k = map(int, input().split())
cur = 0
for c in input():
    if c != 'LR'[cur&1]: k -= 1
    else: cur ^= 1
print(max(0, k))