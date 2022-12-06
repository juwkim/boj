A, a, B, b, P = map(int, input().split())
s, t = sorted([[A, a], [B, b]])
if s[0] <= t[1] and t[0] <= P or s[0] + t[0] <= P:
    print('Yes')
else:
    print('No')