a1, b1 = input()
a2, b2 = input()
print(*sorted((abs(ord(a1) - ord(a2)), abs(ord(b1) - ord(b2)))))