first = input()
seq = input()
n = len(seq)
total = 0
for mask in range(1, 1 << n):
    small = [seq[i] for i in range(n) if (mask >> i) & 1]
    light = [first] + small[:-1]
    good = True
    for i in range(len(small) - 1):
        if light[i+1] == small[i+1] and light[i] + small[i] in "RS SP PR":
            good = False
            break
    total += good
print(total)