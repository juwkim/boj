input()
total = 0
for i, num in enumerate(map(int, input().split())):
    total += min(num, 7) - 2 - i % 2
print(total)