import sys

input = lambda: sys.stdin.readline().rstrip()

S = input()
one, zero = 0, 0
one_count = S.count('1')
zero_count = len(S) - one_count
ans = []
for c in S:
    if c == '0':
        zero += 1
        if zero * 2 <= zero_count:
            ans.append('0')
    else:
        one += 1
        if one * 2 > one_count:
            ans.append('1')
print(*ans, sep="")