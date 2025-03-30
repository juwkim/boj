for _ in range(int(input())):
    N = int(input())
    if N & 1:
        ans = 0
    else:
        ans = 1 << N // 2
    print(ans)