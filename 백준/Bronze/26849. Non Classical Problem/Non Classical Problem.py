buf = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    buf.append(a / b)
print(min(buf), max(buf), sum(buf))