import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

n = int(input())
fish = []
for i in range(1, n + 1):
    m, w = g()
    fish.append([i, 2 * m, w])
res = [0] * (n + 1)
day = 0
while fish:
    dead = len(fish) // 2
    fish.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for i in range(len(fish) // 2):
        i1, m1, w1 = fish[i]
        i2, m2, w2 = fish[-i - 1]
        # if m1 == m2:
        #     dead = i
        #     break
        fish[i][1] += m2 // 2
    for i in range(len(fish) - dead):
        i, m, w = fish.pop()
        res[i] = day
    day += 1
for _ in range(int(input())):
    r, x = g()
    print(("TAK", "NIE")[res[r] < x])