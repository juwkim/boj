N = int(input())
for _ in range(N):
    d, n, s, p = map(int, input().split())
    if d > n * (s - p):
        print('do not parallelize')
    elif d < n * (s - p):
        print('parallelize')
    else:
        print('does not matter')