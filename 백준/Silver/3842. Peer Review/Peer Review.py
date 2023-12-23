import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while True:
    K, N = g()
    if K == N == 0:
        break
    check = [[K, False] for _ in range(N + 1)]
    paper = [[]]
    for _ in range(N):
        my, *l = input().split()
        paper.append([my, list(map(int, l))])
    for i in range(1, N + 1):
        my, l = paper[i]
        viewed = set()
        for num in l:
            if num in viewed:
                check[num][1] = True
                continue
            viewed.add(num)
            if check[num][1]:
                continue
            if paper[num][0] == my or check[num][0] == 0:
                check[num][1] = True
                continue
            check[num][0] -= 1
    problem = 0
    for i in range(1, N + 1):
        if check[i][0] or check[i][1]:
            problem += 1
    if problem:
        print(f"{problem} PROBLEMS FOUND")
    else:
        print("NO PROBLEMS FOUND")