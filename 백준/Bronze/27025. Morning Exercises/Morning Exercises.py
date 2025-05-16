max_len, cur = 0, 0
for _ in range(int(input())):
    top, btm = map(int, input().split())
    if top == 0 and btm == 0:
        cur += 1
        max_len = max(max_len, cur)
    else:
        cur = 0
print(2 * max_len)