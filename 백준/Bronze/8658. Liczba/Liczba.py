n = int(input())
i, j = 2, n-1
while not n % i: i += 1
while not n % j: j -= 1
print(i, j)