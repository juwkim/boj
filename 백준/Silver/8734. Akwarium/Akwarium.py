import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

n = int(input())
fish = []
for i in range(1, n + 1):
    m, w = g()
    fish.append([2 * m, w, i])
res = [0] * (n + 1)
day = 0
while fish:
    dead = len(fish) & 1
    fish.sort(reverse=True)
    for i in range(len(fish) // 2):
        m, _, j = fish.pop()
        fish[i][0] += m // 2
        res[j] = day
    if dead:
        res[fish.pop()[2]] = day
    day += 1
for _ in range(int(input())):
    r, x = g()
    print(("TAK", "NIE")[res[r] < x])