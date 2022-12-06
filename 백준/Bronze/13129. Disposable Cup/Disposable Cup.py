A, B, N = map(int, input().split())
print(*[A*(N-i) + (A+B)*i for i in range(1, N+1)])