import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for tc in range(1, 1 + int(input())):
    n, c, l = g()
    friedns = [[0, 0] for _ in range(l + 1)]
    for _ in range(n):
        num, state = input().split()
        friedns[int(num)][state == 'I'] += 1
    cars = [[] for _ in range(l + 1)]
    for _ in range(c):
        num, cnt = g()
        cars[num].append(cnt)
    ans = 0
    for i in range(1, l + 1):
        sober, intoxicated = friedns[i]
        for j, car in enumerate(sorted(cars[i], reverse=True)):
            if sober <= 0:
                break
            num = min(intoxicated, car - 1)
            car -= num
            intoxicated -= num
            sober -= min(car, max(1, sober - (len(cars[i]) - j) + 1))
        ans += max(sober, 0) + max(intoxicated, 0)
    print(f"Data Set {tc}:\n{ans}")