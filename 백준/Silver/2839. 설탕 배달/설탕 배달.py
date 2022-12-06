N = int(input())
if N == 4 or N == 7:
    print(-1)
else:
    print(N // 5 + N % 5 - 2 * ((N % 5) // 3))