A, B, K = map(int, input().split())
if B % A:
    print(-1)
else:
    l = [A, B]
    for i in range(2 * A, B, A):
        if len(l) == K:
            break
        if i % A == 0 and B % i == 0:
            l.append(i)
    if len(l) == K:
        print(*l)
    else:
        print(-1)