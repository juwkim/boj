remainder = set([])
for _ in range(10):
    remainder.add(int(input()) % 42)

print(len(remainder))