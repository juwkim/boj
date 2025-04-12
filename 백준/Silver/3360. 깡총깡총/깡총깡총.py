q, r = divmod(int(input()), 6)
print(((3 * q + 2) * q + (q + 1) * (r + 1) - (r > 0)) % 1000000)