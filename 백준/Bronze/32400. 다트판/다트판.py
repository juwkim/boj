a = [*map(int, open(0).read().split())]
i = a.index(20)
alice = (a[i - 1] + a[i] + a[(i + 1) % 20]) * 20
bob = sum(a) * 3
print(("Tie", "Alice", "Bob")[(alice > bob) - (alice < bob)])