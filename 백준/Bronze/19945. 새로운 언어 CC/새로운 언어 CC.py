n = int(input())
print(len(bin(n)[2:]) if n >= 0 else 32)