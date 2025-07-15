conditions = []
for line in map(str.rstrip, open(0)):
    if line == '.':
        ans = "No pizza can satisfy these requests."
        for mask in range(1 << 16):
            if all(any(((mask >> (ord(t) - ord('A'))) & 1) == req for t, req in cond) for cond in conditions):
                topping = ''.join(chr(ord('A') + i) for i in range(16) if (mask >> i) & 1)
                ans = f"Toppings: {topping}"
                break
        print(ans)
        conditions.clear()
    elif line.endswith(';'):
        conditions.append([(line[i + 1], line[i] == '+') for i in range(0, len(line) - 1, 2)])