import sys
input = sys.stdin.readline
g = lambda: [*map(float, input().split())]

while N:=int(input()):
    x, y, r = g()
    nums = [g() for _ in range(N - 1)]
    cnt = 0
    for dx in range(-100, 101):
        for dy in range(-100, 101):
            p, q = x + dx * r / 100, y + dy * r / 100
            if (p - x) ** 2 + (q - y) ** 2 > r ** 2:
                continue
            if any((p - a) ** 2 + (q - b) ** 2 <= r ** 2 for a, b, r in nums):
                cnt += 1
    print(f"{cnt / 31416:.2f}")