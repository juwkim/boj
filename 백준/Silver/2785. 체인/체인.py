ans = 0
N = int(input())
for i, num in enumerate(sorted(map(int, input().split())), 1):
    if ans + num < N - i - 1:
        ans += num
        continue
    if ans + num == N - i - 1:
        ans = N - i - 1
    else:
        ans = N - i
    break
print(ans)