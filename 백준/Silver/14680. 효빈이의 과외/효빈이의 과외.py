g = lambda: tuple(map(int, input().split()))
flag = True
N = int(input())
X, Y = g()
A = [g() for _ in range(X)]
for _ in range(N - 1):
    P, Q = g()
    if Y != P:
        flag = False
        break
    B = [*zip(*[g() for _ in range(P)])]
    A = [[sum(a * b for a, b in zip(A[i], B[j])) for j in range(Q)] for i in range(X)]
    Y = Q
if flag:
    ans = sum(sum(line) for line in A) % 1000000007
else:
    ans = -1
print(ans)