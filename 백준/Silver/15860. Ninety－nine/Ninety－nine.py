num, idx = [1, 2], 0
print(num[idx], flush=True)
while True:
    cur = int(input())
    r = cur % 3
    if r:
        cur += 3 - r
    else:
        idx ^= 1
        cur += num[idx]
    print(cur, flush=True)
    if cur == 99:
        break