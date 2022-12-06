def solve(C, V, L):
    global t
    if L == 1:
        return V
    elif L == 2:
        return (C + V) * V
    return (C * V * solve(C, V, L-2) % t + V * solve(C, V, L-1) % t) % t

t = 10**9 + 7
for i in range(1, 1+int(input())):
    s = solve(*map(int, input().split()))
    print(f'Case #{i}: {s}')