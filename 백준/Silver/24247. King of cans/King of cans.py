x, y = map(int, input().split())
print(min((x * 2 + y // 2 * 6) // 100, x // 2))