import sys
input = sys.stdin.readline
from collections import Counter
for tc in range(1, 1 + int(input())):
    cnt = Counter()
    for _ in range(2 * int(input()) - 1):
        cnt += Counter(map(int, input().split()))
    ans = [k for k, v in sorted(cnt.items()) if v % 2]
    print(f'Case #{tc}:', *ans)