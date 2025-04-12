q, r = divmod(int(input()), 6)
print(((3 * q + r) * (q + 1) + (r == 0)) % 1000000)