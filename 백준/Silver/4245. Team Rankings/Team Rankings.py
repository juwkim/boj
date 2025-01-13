import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations, permutations

while N:=int(input()):
    l = [input() for _ in range(N)]
    ans, score = None, 1e9
    for S in permutations("ABCDE"):
        cnt = 0
        for T in l:
            for a, b in combinations("ABCDE", 2):
                if (S.index(a) - S.index(b)) * (T.index(a) - T.index(b)) < 0:
                    cnt += 1
        if cnt < score:
            ans, score = S, cnt
    print(f"{''.join(ans)} is the median ranking with value {score}.")