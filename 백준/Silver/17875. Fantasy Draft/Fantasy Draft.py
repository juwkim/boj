import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
owners_iter = [iter(input().split()[1:]) for _ in range(n)]
rank_iter = iter(input() for _ in range(int(input())))
ans = [[] for _ in range(n)]
taken = set()
for _ in range(k):
    for i in range(n):
        for candidate in owners_iter[i]:
            if candidate not in taken:
                picked = candidate
                break
        else:
            for candidate in rank_iter:
                if candidate not in taken:
                    picked = candidate
                    break
        ans[i].append(picked)
        taken.add(picked)
for row in ans:
    print(' '.join(row))