N, K, *A = map(int, open(0).read().split())
if all((A[i] - i) % K == 0 for i in range(N)):
    print("Yes")
else:
    print("No")