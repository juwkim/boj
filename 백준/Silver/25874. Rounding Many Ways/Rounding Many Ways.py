ans, t, N = [], 1, int(input())
while t <= N:
    if N % t == 0: ans.append(t)
    s = t
    while (s:=s*5) <= N and N % s == 0:
        ans.append(s)
    t <<= 1
print(len(ans))
print(*sorted(ans), sep='\n')