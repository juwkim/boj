N = int(input())
print(chr((N - 1) % 8 + 97), (N + 7) // 8, sep="")