import sys
input = sys.stdin.readline
g = lambda: [*map(float, input().split())]

while N:=int(input()):
    x, y, r = g()
    nums = [g() for _ in range(N - 1)]
    ans = 0
    for dx in range(-50, 51):
        for dy in range(-50, 51):
            p, q = x + dx * r / 50, y + dy * r / 50
            ans += (p - x) ** 2 + (q - y) ** 2 <= r ** 2 and any((p - a) ** 2 + (q - b) ** 2 <= r ** 2 for a, b, r in nums)
    print(f"{ans / 7854:.2f}")