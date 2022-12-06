g = lambda x: int(x**.5)**2 != x

M = int(input())
N = int(input())

squares = [i**2 for i in range(int(M**.5) + g(M), int(N**.5) + 1)]
if squares:
    print(sum(squares), squares[0])
else:
    print(-1)