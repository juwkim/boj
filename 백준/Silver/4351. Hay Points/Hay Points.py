import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
m, n = g()
dic = {}
for _ in range(m):
    name, cost = input().split()
    dic[name] = int(cost)
for _ in range(n):
    ans = 0
    while (s:= input()) != '.':
        for word in s.split():
            if word in dic:
                ans += dic[word]
    print(ans)