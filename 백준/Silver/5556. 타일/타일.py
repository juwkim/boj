N = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    s = min(a, b, N + 1 - a, N + 1 - b) - 1
    print(1 + s % 3)