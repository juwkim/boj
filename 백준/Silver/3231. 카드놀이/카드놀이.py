N = int(input())
idx_list = [None] * (N + 1)
for i in range(1, N + 1):
    idx_list[int(input())] = i
ans = sum(a > b for a, b in zip(idx_list[1:], idx_list[2:]))
print(ans)