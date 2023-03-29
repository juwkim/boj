from collections import Counter

cnt = Counter(input())
U, D, P, C = [cnt[i] for i in 'UDPC']
ans = []

if U + C > (D + P + 1) // 2:
    ans.append('U')
if D + P:
    ans.append('DP')
if ans:
    print(*ans, sep='')
else:
    print('C')