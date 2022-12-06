S, D = input().split()
P = bin(int(S.replace('A', '0').replace('B', '1')[::-1], 2) + int(D))[:1:-1]
ans = P.replace('0', 'A').replace('1', 'B')
ans += 'A' * (len(S) - len(ans))
print(ans)