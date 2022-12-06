n = int(input())
arr = [0] * (n + 1)
for i in range(1, 1 + n):
    arr[int(input())] = i
print(*arr[1:])