cnt = 0
N = int(input())
while True:
    r, q = divmod(N, 3)
    cnt += 1
    if not r or (r == 1 and not q):
        break
    N = r + (q != 0)
print(cnt)