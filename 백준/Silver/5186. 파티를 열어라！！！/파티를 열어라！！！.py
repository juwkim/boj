import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for tc in range(1, 1 + int(input())):
    n, c, l = g()
    friedns = [[0, 0] for _ in range(l)]
    for _ in range(n):
        num, state = input().split()
        friedns[int(num) - 1][state == 'I'] += 1
    cars = [[] for _ in range(l)]
    for _ in range(c):
        num, cnt = g()
        cars[num - 1].append(cnt)
    ans = 0
    for i in range(l):
        sober, intoxicated = friedns[i]
        for j, car in enumerate(sorted(cars[i], reverse=True)):
            if sober == 0:
                break
            num = min(intoxicated, car - 1)
            intoxicated -= num
            sober -= min(car - num, max(1, sober - len(cars[i]) + j + 1))
        ans += sober + intoxicated
    print(f"Data Set {tc}:\n{ans}")