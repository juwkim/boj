k = int(input())
i = 1
while len(str(i**3)) < k:
    k -= len(str(i**3))
    i += 1
print(str(i**3)[k-1])