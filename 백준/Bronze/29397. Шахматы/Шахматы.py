a = sum(map(ord, input()))
b = sum(map(ord, input()))
print(["YES", "NO"][(a - b) & 1])