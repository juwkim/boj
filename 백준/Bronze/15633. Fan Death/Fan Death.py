n = int(input())
total = 0
for i in range(1, n+1):
    if n%i == 0:
        total += i
print(5*total - 24)