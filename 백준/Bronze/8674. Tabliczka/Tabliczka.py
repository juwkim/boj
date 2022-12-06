a, b = map(int, input().split())
print(min(a, b) if a%2 and b%2 else 0)