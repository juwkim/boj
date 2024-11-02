N = int(input())
a = sorted(map(int, input().split()))
ans = 2 * sum(a[N//2:])
if N & 1:
    ans -= a[N//2]
print(ans)