for _ in range(int(input())):
    l = [*map(int, input().split())]
    a, b = l[:3], l[3:]
    idx = (sum(a) > sum(b)) + (a > b) * 2
    print(*l,('none','count','color','both')[idx],'',sep='\n')