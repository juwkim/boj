N = int(input())
s = input()
ans = 'NO'
for l in range(1, N):
    t = sum(a != b for a, b in zip(s[:l], s[-l:]))
    if t == 1:
        ans = 'YES'
        break
print(ans)