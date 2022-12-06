g = lambda: [*map(int, input().split())]

N = int(input())
score = [0] * 101
for num in g():
    score[num] += 100

check = [4, 11, 23, 40, 60, 77, 89, 96, 100]
cnt = 0
idx = 0
before = 0
for i in range(100, -1, -1):
    cnt += score[i]
    while True:
        if cnt >= check[idx] * N:
            print((cnt - before) // 100)
            idx += 1
            before = cnt
            if idx == 9:
                break
        else:
            break
    if idx == 9:
        break
for _ in range(9 - idx):
    print(0)