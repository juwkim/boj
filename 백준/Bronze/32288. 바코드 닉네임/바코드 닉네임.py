input()
print(*[chr(ord(c) ^ 32) for c in input()], sep='')