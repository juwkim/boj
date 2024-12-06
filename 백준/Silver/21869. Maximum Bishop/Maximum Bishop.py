N = int(input())
if N == 1:
    print("1\n1 1")
else:
    print(2 * N - 2)
    for i in range(1, N + 1):
        print(1, i)
    for i in range(2, N):
        print(N, i)