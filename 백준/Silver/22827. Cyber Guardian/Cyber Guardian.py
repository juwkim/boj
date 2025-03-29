import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while (l:=g()) != [0, 0]:
    n, m = l
    rule = [input().split() for _ in range(n)][::-1]
    ans = []
    for _ in range(m):
        src, dst, msg = input().split()
        flag = False
        for t, s, d in rule:
            if all(a == '?' or a == b for a, b in zip(s, src)) and all(a == '?' or a == b for a, b in zip(d, dst)):
                flag = t[0] == 'p'
                break        
        if flag:
            ans.append((src, dst, msg))
    print(len(ans))
    for l in ans:
        print(*l)