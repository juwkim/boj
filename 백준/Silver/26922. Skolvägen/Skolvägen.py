N, S = 0, 1
for c in input():
    match c:
        case 'N':
            N, S = min(N + 1, S + 1), min(S, N + 2)
        case 'S':
            N, S = min(N, S + 2), min(S + 1, N + 1)
        case 'B':
            N, S = min(N + 1, S + 2), min(S + 1, N + 2)
ans = min(N, S + 1)
print(ans)