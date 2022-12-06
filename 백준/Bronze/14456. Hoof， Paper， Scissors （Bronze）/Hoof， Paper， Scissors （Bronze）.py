N = int(input())
cnt = [0, 0]
for _ in range(N):
    s = input()
    if s[0] == s[2]:
        pass
    else:
        cnt[s in ['1 2', '2 3', '3 1']] += 1
print(max(cnt))