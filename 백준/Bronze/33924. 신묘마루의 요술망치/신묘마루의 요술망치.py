N, M = map(lambda x: int(x) - 1, input().split())
input()
for c in input():
    match c:
        case 'A':
            N = (2, 3, 0, 1)[N]
        case 'B':
            N = (1, 0, 3, 2)[N]
            M = (1, 0)[M]
        case 'C':
            N = (3, 2, 1, 0)[N]
            M = (1, 0)[M]
        case 'D':
            if N == 0 and M == 0:
                M = 1
            elif N == 3 and M == 1:
                M = 0
            elif M == 0:
                N -= 1
            else:
                N += 1
print(N + 1, M + 1)