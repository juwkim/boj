group = [input() for _ in [0]*6].count('W') // -2 + 4
print([group, -1][group == 4])