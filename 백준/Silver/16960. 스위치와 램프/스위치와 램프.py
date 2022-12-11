g = lambda: [*map(int, input().split())]

N, M = g()
dic = {i: 0 for i in range(1, M + 1)}
switches = []
for _ in range(N):
    _, *switch = g()
    for lamp in switch:
        dic[lamp] += 1
    switches.append(switch)
ans = 0
for switch in switches:
    if all(dic[lamp] > 1 for lamp in switch):
        ans = 1
        break
print(ans)