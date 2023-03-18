from collections import Counter

for _ in range(int(input())):
    cnt = Counter(input())
    ans = sum(sorted(cnt.values())[:-2])
    print(ans)