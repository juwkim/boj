import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
even, odd = 0, 0
for num in g():
    if num & 1:
        odd += 1
    else:
        even += 1
if odd > even:
    cnt = (odd - even + 2) // 3
    odd -= cnt * 2
    even += cnt
print(odd + min(odd + 1, even))