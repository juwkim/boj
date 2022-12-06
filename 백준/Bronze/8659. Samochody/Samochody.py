n = int(input())
cars = [*map(int, input().split())]
cnt = 0
zeros = 0
for i in range(n):
    if cars[i]:
        cnt += zeros
    else:
        zeros += 1
print(cnt)