g = lambda: [*map(int, input().split())]

r, c = g()
Map = [g() for _ in range(r)]
Map += [*zip(*Map)]
ans = 0
for i in range(r+c):
    for j in range(len(Map[i])):
        ans += all(Map[i][j] > num for num in Map[i][:j])
        ans += all(Map[i][j] > num for num in Map[i][j+1:])
print(ans)