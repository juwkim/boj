M, N = map(int, input().split())
total = 0
while M > 3 and N > 3:
    total += 4
    M -= 2
    N -= 2
if N <= 3:
    if M == 2:
        total += 2
    elif M == 3:
        total += N + M - 2
    else:
        total += 2 * N - 1
else:
    total += 2 * M - 2
print(total)  