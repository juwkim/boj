g = lambda: [*map(int, input().split())]

ans, cur = 0, None
wait = 0
for _ in range(int(input())):
    time, direction = map(int, input().split())
    if cur == None:
        ans = time + 10
        cur = direction
    elif cur == direction:
        if not wait or time < ans:
            ans = time + 10
        else:
            cur ^= 1
            ans += 10
            wait = time
    else:
        if time > ans:
            cur ^= 1
            ans = time + 10
            wait = 0
        else:
            wait = time
if wait:
    ans += 10
print(ans)