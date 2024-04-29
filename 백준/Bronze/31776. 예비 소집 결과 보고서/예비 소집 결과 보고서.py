ans = 0
for _ in range(int(input())):
    t1, t2, t3 = map(int, input().split())
    if t1 != -1 and (t1 <= t2 <= t3 or (t1 <= t2 and t3 == -1) or (t2 == t3 == -1)):
        ans += 1
print(ans)