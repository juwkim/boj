n = int(input())
ans = n
for i in range(1, n - 1, 2):
    print('?', i, i + 1, flush=True)
    if input() == "equal":
        continue
    print('?', i, n, flush=True)
    if input() == "equal":
        ans = i + 1
    else:
        ans = i
    break
if n % 2 == 0 and ans == n:
    print('?', 1, n, flush=True)
    if input() == "equal":
        ans = n - 1
    else:
        ans = n
print('!', ans)