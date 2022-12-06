N = int(input())
print(sorted(set(input() for _ in range(N)), key=float)[1])