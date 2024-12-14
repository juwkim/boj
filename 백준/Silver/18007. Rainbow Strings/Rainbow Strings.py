from collections import Counter

cnt = Counter(input())
ans = 1
for k, v in cnt.items():
    ans = ans * (v + 1) % 11092019
print(ans)