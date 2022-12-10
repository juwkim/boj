N = int(input())
S = input().split()
T = sorted(S, key=lambda x: ('BSGPD'.index(x[0]), -int(x[1:])))
ans = None
for a, b in zip(S, T):
    if a != b:
        ans = (b, a)
        break
if ans:
    print('KO')
    print(*ans)
else:
    print('OK')