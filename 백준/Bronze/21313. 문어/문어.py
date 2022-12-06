N = int(input())
print(*['1 2' for _ in range(N//2)], 3 if N % 2 else '')