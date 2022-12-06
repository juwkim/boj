N, L, D = map(int, input().split())
s, t = L, D
flag = 1
while s != N*L + 5*(N-1):
    if t < s:
        t += D
    elif t > s + 4:
        s += L + 5
    else:
        flag = 0
        break
if flag:
    while t < s:
        t += D
print(t)