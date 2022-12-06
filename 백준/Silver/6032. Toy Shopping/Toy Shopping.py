g = lambda: [*map(int, input().split())]

N = int(input())
buf = [g() for _ in range(N)]
ans = [*range(N)]
ans.sort(key=lambda x: buf[x][0] / buf[x][1], reverse=True)

val = 0
for i in range(3):
    val += buf[ans[i]][1]

print(val)
for i in range(3):
    print(ans[i] + 1)