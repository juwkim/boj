n, k, *a = map(int, open(0).read().split())
ans, front, bottle = 0, 0, set()
for num in a:
    if num in bottle:
        front += 1
    else:
        bottle.add(num)
        ans += front
        if len(bottle) == k:
            break
print(ans if len(bottle) == k else -1)