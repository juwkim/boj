V, E = 999, 1501
a, b = 60, 61
print(f"{V} {E}")
for _ in range(E):
    if b > 61:
        b = a
        a -= 1
    print(f"{a} {b}")
    b += 1