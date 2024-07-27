k = int(input())
b = int(input())
for i in range(2, k + 1):
    x, y = map(int, input().split())
    j = b + 1
    if b > 1 and i + b - 1 + x + y & 1:
        j = b - 1
    elif i + b + x + y & 1:
        j = b
    print(i, j, flush=True)