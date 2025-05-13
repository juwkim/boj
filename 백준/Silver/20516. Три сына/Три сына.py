q, r = divmod(int(input()), 3)
print(q - 1, q + (r == 2), q + 2 - (r == 0))