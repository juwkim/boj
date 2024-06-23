import sys
input = sys.stdin.readline

p, m = map(int, input().split())
ans = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    for i in range(len(ans)):
        if len(ans[i]) < m and ans[i][0][0] - 10 <= l <= ans[i][0][0] + 10:
            ans[i].append((l, n))
            break
    else:
        ans.append([(l, n)])
for room in ans:
    print(("Waiting!", "Started!")[len(room) == m])
    for l, n in sorted(room, key=lambda x: x[1]):
        print(l, n)