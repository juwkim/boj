N = int(input())
ans = 0
for num in sorted(map(int, input().split()), reverse=True):
    if num < ans:
        break
    ans += 1
print(ans)