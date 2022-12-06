import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while (s:= g())[0]:
    N, Q = s
    dic = {}
    for _ in range(N):
        name, *l = input().split()
        E, W = map(int, l)
        dic[name] = [W - E + 1, W]
    for _ in range(Q):
        ans = 'Unknown'
        year = int(input())
        for name in dic:
            a, b = dic[name]
            if a <= year <= b:
                ans = f'{name} {year-a+1}'
                break
        print(ans)