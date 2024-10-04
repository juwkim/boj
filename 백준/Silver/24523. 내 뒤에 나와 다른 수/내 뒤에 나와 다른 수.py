N, prev, *A = map(int, open(0).read().split())
cnt = 1
for i, num in enumerate(A, 2):
    if num == prev:
        cnt += 1
    else:
        for _ in range(cnt):
            print(i, end=' ')
        cnt = 1
        prev = num
for _ in range(cnt):
    print(-1, end=' ')