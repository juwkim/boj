n = int(input())

winner, max_S, min_C, min_L = 0, 0, 50, 179
for i in range(1, n+1):
    S, C, L = map(int, input().split())
    if S > max_S:
        winner, max_S, min_C, min_L = i, S, C, L
    elif S == max_S and C < min_C:
        winner, max_S, min_C, min_L = i, S, C, L
    elif S == max_S and C == min_C and L <= min_L:
        winner, max_S, min_C, min_L = i, S, C, L
print(winner)