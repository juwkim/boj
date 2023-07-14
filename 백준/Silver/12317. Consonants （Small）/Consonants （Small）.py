for tc in range(1, 1 + int(input())):
    L, N = input().split()
    N = int(N)
    ans = 0
    for i in range(len(L) - (N - 1)):
        for j in range(N - 1, len(L)):
            cnt, cur = 0, 0
            for c in L[i:j+1]:
                if c in 'aeiou':
                    cnt = max(cnt, cur)
                    if cnt >= N:
                        break
                    cur = 0
                else:
                    cur += 1
                    if cur >= N:
                        break
            cnt = max(cnt, cur)
            if cnt >= N:
                ans += 1
    print(f"Case #{tc}: {ans}")