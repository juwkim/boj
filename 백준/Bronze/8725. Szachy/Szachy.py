n = int(input())
print(sum(int(max(input().split() + ['0'], key=int)) for _ in range(n)))