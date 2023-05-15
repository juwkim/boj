while (s:= input()) != '0 0':
    A, C = map(int, s.split())
    ans, cur = 0, 0
    for num in map(int, input().split()):
        ans += max(0, A - num - cur)
        cur = A - num
    print(ans)