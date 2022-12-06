P, N = map(int, [input(), input()])
stones = [0] * 100
for _ in[0]*N:
    num, direction = input().split()
    if direction == 'L':
        for i in range(int(num)-1):
            stones[i] += 1
    else:
        for i in range(int(num), 100):
            stones[i] += 1
color = [0, 0, 0]
for stone in stones:
    color[stone % 3] += 1

print(*map(lambda x: f'{P*x/100:#.2f}', color))