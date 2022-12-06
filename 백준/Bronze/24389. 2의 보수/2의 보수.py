N = int(input())
a = bin(2**32 + (N ^ -N))
print(a.count('1'))