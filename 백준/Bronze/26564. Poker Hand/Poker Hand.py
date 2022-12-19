from collections import Counter
for _ in range(int(input())):
    cnt = Counter(i[0] for i in input().split())
    print(max(cnt.values()))