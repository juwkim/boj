N = int(input())
count = 0
for i in range(1, int(N**.5)+1):
    if N%i == 0:
        count += 1 + (N != i**2)
print(count)