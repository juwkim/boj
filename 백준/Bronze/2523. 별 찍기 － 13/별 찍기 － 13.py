N = int(input())
for i in range(-N + 1, N):
    print('*' * (N - abs(i)))