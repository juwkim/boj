g = lambda: [*map(int, input().split())]

buf = [g() for _ in range(int(input()))]
Max_cnt, ans = -1, None
for i in range(4):
    for j in range(i + 1, 5):
        cnt = sum(stu[i] and stu[j] for stu in buf)
        if cnt > Max_cnt:
            Max_cnt = cnt
            ans = (i, j)

day = [0] * 5
day[ans[0]] = 1
day[ans[1]] = 1
print(Max_cnt)
print(*day)  