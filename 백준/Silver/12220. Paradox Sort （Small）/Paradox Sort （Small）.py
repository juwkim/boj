import sys
input = sys.stdin.readline
from itertools import permutations

for tc in range(1, 1 + int(input())):
    N, A = map(int, input().split())
    a = [input() for _ in range(N)]
    ans = "IMPOSSIBLE"
    for l in permutations(range(N)):
        cur, *nums = l
        for num in nums:
            if a[num][cur] == 'Y':
                cur = num
        if cur == A:
            ans = " ".join(map(str, l))
            break
    print(f"Case #{tc}: {ans}")