g = lambda: [*map(int, input().split())]

condo = [g() for _ in range(int(input()))]
cnt = 0
for i in range(len(condo)):
    D, C = condo[i]
    flag = True
    for j in range(len(condo)):
        if i != j:
           if condo[j][1] < C:
               if condo[j][0] <= D:
                   flag = False
                   break
           if condo[j][0] < D:
               if condo[j][1] <= C:
                   flag = False
                   break
    cnt += flag               
print(cnt)