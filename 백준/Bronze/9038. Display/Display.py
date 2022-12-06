for _ in range(int(input())):
    w = int(input())
    ans = 0
    cur = -1
    for word in input().split():
        tmp = cur + len(word) + 1
        if tmp == w:
            ans += 1
            cur = -1
        elif tmp > w:
            ans += 1
            cur = len(word)
        else:
            cur = tmp
    print(ans + (cur != -1))