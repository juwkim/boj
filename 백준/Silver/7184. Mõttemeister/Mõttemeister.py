import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
nums = []
for _ in range(N):
    guess, A, B = input().split()
    nums.append((guess, int(A), int(B)))
ans = []
for check in map(lambda s: str(s).zfill(4), range(10000)):
    cnt = Counter(check)
    for guess, A, B in nums:
        a, b = 0, 0
        visited = bytearray(4)
        cnt2 = Counter(guess)
        a = sum(min(cnt[i], cnt2[i]) for i in map(str, range(10)))
        b = sum(guess[i] == check[i] for i in range(4))
        if a != A or b != B:
            break
    else:
        ans.append(check)
print(len(ans))
print(*ans, sep='\n')