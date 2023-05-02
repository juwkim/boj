a, b = 224584605939537911, 18135696597948930

n = int(input())
if n > 27:
    assert n != 28
    print(-1)
else:
    ans = [a + b * i for i in range(n)]
    print(*ans)