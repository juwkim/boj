res = set()
for _ in range(int(input())):
    res.add(input()[0])

for c in range(65, 92):
    if chr(c) not in res:
        break
print(c - 65)