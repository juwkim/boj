t = 10**9 + 7
ans = [[[0 for _ in range(501)] for _ in range(51)] for _ in range(51)]
for C in range(1, 51):
    for V in range(1, 51):
        ans[C][V][1], ans[C][V][2] = V, (C + V) * V
        for L in range(3, 501):
            ans[C][V][L] = (C * ans[C][V][L-2] + ans[C][V][L-1]) * V % t

for i in range(1, 1+int(input())):
    C, V, L = map(int, input().split())
    print(f'Case #{i}: {ans[C][V][L]}')