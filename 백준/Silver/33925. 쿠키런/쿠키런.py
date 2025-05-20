N, J, S, H, K = map(int, input().split())
stage = [input() for _ in range(3)]
jump = 0
for j in range(N):
    if stage[0][j] == 'v':
        S -= 1
    elif stage[1][j] == '^':
        jump += 1
    elif stage[2][j] == '^':
        J -= 1
H += min(0, S * K) + min(0, J * K) - max(0, (jump - max(0, J >> 1)) * K)
if H > 0:
    print(H)
else:
    print(-1)