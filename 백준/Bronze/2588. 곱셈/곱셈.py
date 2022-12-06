A = int(input())
B = int(input())

print(A * (B % 10))
print(A * ((B % 100) // 10))
print(A * (B // 100))
print(A * B)