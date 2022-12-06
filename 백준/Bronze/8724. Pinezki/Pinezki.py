N = int(input())
a = [0] + [*map(int, input().split())] + [0]
temp = []
for i in range(N + 2):
    if a[i] == 0:
        temp += [i]
print(max(b - a for a, b in zip(temp, temp[1:])) - 1)