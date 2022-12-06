A = int(input())
B = int(input())
C = int(input())
mul = list(str(A * B * C))

for i in range(10):
    print(mul.count(str(i)))