L, D, X = [int(input()) for _ in range(3)]
while True:
    if sum(int(digit) for digit in str(L)) == X:
        break
    L += 1
while True:
    if sum(int(digit) for digit in str(D)) == X:
        break
    D -= 1
print(L, D, sep='\n')