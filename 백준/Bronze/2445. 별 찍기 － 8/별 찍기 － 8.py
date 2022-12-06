N = int(input())
for i in range(1, N):
    print(('*' * i).ljust(N) + ('*' * i + ' ').rjust(N + 1))
for i in range(N, 0, -1):
    print(('*' * i).ljust(N) + ('*' * i + ' ').rjust(N + 1))