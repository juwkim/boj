buf = []
for _ in range(int(input())):
    buf.append(sum([*map(int, input().split())][1:]))
buf.sort(reverse=True)
ans = 0
for i in range(len(buf)):
    ans += (i + 1) * buf[i]
print(ans)