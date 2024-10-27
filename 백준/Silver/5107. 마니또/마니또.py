import sys
input = sys.stdin.readline

tc = 1
while N:=int(input()):
    dic = {}
    names = set()
    for _ in range(N):
        a, b = input().split()
        dic[a] = b
        names.add(a)
        names.add(b)
    visited, cnt = set(), 0
    for name in names:
        if name in visited:
            continue
        visited.add(name)
        start, cur = name, name
        while True:
            if cur not in dic:
                break
            cur = dic[cur]
            if cur == start:
                cnt += 1
                break
            if cur in visited:
                break
            visited.add(cur)
    print(tc, cnt)
    tc += 1