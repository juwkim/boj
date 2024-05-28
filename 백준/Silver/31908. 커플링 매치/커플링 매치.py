from collections import defaultdict

dic = defaultdict(list)
for _ in range(int(input())):
    p, s = input().split()
    if s != '-': dic[s].append(p)

ans = [v for v in dic.values() if len(v) == 2]
print(len(ans))
for v in ans:
    print(*v)