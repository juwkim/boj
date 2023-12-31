for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))
    L = [L[0]] + L + [L[-1]]
    ans = max(L[i + 2] - L[i] for i in range(N))
    print(ans)