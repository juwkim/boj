N = int(input())
cur = 1

while True:
    if N < cur:
        ans = cur - N
        break
    N -= cur
    cur += 1
    if N < cur:
        ans = 0
        break
    N -= cur
    cur += 1
print(ans)