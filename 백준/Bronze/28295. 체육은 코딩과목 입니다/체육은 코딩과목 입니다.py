d = 0
for _ in range(10):
    t = int(input())
    if t == 3:
        t = -1
    d += t
print("NESW"[d % 4])