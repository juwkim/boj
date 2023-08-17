cnt = [2, 1, 1, 1, 2,
       2, 1, 3, 3, 2,
       3, 1, 1, 1, 1,
       1, 1, 2, 1, 2,
       1, 1, 1, 2, 2,
       1]

ans = 0
for c in input():
    ans += cnt[ord(c) - ord('A')]
print(ans)