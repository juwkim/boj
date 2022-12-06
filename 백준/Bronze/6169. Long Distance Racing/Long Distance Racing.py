g = lambda: [*map(int, input().split())]
M, T, U, F, D = g()
for i in range(T):
    M -= [U + D, 2 * F][input() == 'f']
    if M < 0:
        print(i)
        break