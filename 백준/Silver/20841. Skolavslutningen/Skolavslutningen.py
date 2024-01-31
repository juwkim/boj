N, M, K = map(int, input().split())
board = [input() for _ in range(N)]

check = set()
for l in board:
    for c in l:
        check.add(c)
# assert len(check) == K

Set, cur = set(), 0
cnt = 0
for l in map(set, zip(*board)):
    cnt += 1
    if not Set & l:
        cur += 1
    Set |= l

cur += K - len(check)
print(cur)