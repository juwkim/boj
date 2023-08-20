n = int(input())
cnt = input().count('1')
ans = max(0, (n + 1) // 2 - cnt)
print(ans)