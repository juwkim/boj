for _ in range(int(input())):
    k, w = map(int, input().split())
    ans = k * w
    prev = input()
    for _ in range(w - 1):
        cur = input()
        overlap = k
        while overlap and prev[k - overlap:] != cur[:overlap]:
            overlap -= 1
        ans -= overlap
        prev = cur
    print(ans)