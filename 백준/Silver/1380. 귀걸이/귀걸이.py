S = lambda: input().split()
I = lambda: int(input())

cnt = 1
while n:= I():
    names = [input() for _ in range(n)]
    res = set()
    for _ in range(2*n-1):
        num = int(S()[0])
        if num in res:
            res.remove(num)
        else:
            res.add(num)
    print(cnt, names[res.pop()-1])
    cnt += 1