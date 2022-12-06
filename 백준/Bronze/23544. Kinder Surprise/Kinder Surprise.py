n = int(input())
buf = set()
for _ in range(n):
    buf.add(input())
print(n - len(buf))