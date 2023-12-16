import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

dic = defaultdict(int)
for _ in range(int(input())):
    num = int("".join(i for i in input() if i.isdigit()))
    dic[num] += 1

ans = [k for k, v in dic.items() if v <= 5]
print(len(ans))
for i in ans:
    print(i)