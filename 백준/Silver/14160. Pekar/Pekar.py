g = lambda: map(int, input().split())
input()
ans = -1
T_sum, A_sum = -1, 0
for T, A in zip(g(), g()):
    T_sum += T
    A_sum += A
    ans = max(ans, T_sum // A_sum)
print(ans * 5 + 5)