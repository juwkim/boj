g = lambda: [*map(int, input().split())]

dic = {}
stu = [g() for _ in range(int(input()))]
stu.sort(key=lambda x: -x[2])

cnt = 0
idx = 0
while cnt < 3:
    nation = stu[idx][0]
    if dic.get(nation):
        if dic.get(nation) < 2:
            dic[nation] += 1
            cnt += 1
            print(*stu[idx][:2])
    else:
        dic[nation] = 1
        cnt += 1
        print(*stu[idx][:2])
    idx += 1