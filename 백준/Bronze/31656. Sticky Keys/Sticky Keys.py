prev = ""
for c in input():
    if c != prev:
        print(c, end="")
        prev = c