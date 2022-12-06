while (s:= input())[:2] != '0 ':
    T, N = map(int, s.split())
    ans = 3 * N
    for _ in range(T):
        ans -= int(input().split()[1])
    print(ans)