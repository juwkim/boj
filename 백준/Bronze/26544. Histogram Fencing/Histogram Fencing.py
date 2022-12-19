g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    N = int(input())
    A, B = g(), g()
    ans = sum(A) * 2 + B[-1]
    prev = 0
    for num in B:
        ans += abs(num - prev)
        prev = num
    print(ans)