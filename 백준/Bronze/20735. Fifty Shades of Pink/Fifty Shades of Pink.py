cnt = 0
for _ in range(int(input())):
    s = input().lower()
    cnt += ('pink' in s) or ('rose' in s)
print(cnt if cnt else 'I must watch Star Wars with my daughter')