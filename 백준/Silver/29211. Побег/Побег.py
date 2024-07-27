k = int(input())
b = int(input())
for i in range(2, k + 1):
    x, y = map(int, input().split())
    if b > 1 and (i + b - 1) % 2 != (x + y) % 2:
        print(i, b - 1, flush=True)
    elif (i + b) % 2 != (x + y) % 2:
        print(i, b, flush=True)
    else:
        print(i, b + 1, flush=True)