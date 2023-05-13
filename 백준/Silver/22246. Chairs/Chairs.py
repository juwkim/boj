log = []
for _ in range(int(input())):
    a, b = input().split()
    log.append((a, 0))
    log.append((b, 1))

ans, cur = 0, 0
for _, flag in sorted(log):
    if flag == 0:
        cur += 1
    else:
        cur -= 1
    ans = max(ans, cur)
print(ans)