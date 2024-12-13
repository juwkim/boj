from itertools import combinations, zip_longest

N = int(input())
a = [input()[::-1] for _ in range(N)]
ans = 1
for l in range(N, 1, -1):
    for s in combinations(a, l):
        if all(sum(map(int, p)) < 10 for p in zip_longest(*s, fillvalue=0)):
            ans = l
            break
    if ans == l:
        break
print(ans)