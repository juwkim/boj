buf = [bytearray(1440) for _ in range(6)]
ans, time, num = "TAIP", 0, None
for i in range(1, 11):
    d, s1, e1, s2, e2 = map(int, input().split())
    t1, t2 = s1 * 60 + e1, s2 * 60 + e2
    time += t2 - t1
    for j in range(t1, t2):
        if buf[d][j]:
            ans = "NE"
            num = buf[d][j], i
            break
        buf[d][j] = i
    if ans == "NE":
        break
print(ans)
if ans == "TAIP":
    print(*divmod(time, 60))
else:
    print(*num)