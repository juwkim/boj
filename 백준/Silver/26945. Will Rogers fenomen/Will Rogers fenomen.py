input = __import__('sys').stdin.readline
g = lambda: tuple(map(int, input().split()))

N, M = g()
A, B = g(), g()
mean_A, mean_B = sum(A) / N, sum(B) / M
ans = None
if mean_A < mean_B:
    for num in B:
        if mean_A < num < mean_B:
            ans = num, 'A'
            break
elif mean_B < mean_A:
    for num in A:
        if mean_B < num < mean_A:
            ans = num, 'B'
            break
if ans:
    print(*ans)
else:
    print('NEJ')    