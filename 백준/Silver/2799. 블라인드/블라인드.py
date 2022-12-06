dic = {
    "................": 0,
    "****............": 0,
    "********........": 0,
    "************....": 0,
    "****************": 0
}
M, N = map(int, input().split())
for _ in range(M):
    input()
    buf = [input().split('#')[1:-1] for _ in range(4)]
    for a, b, c, d in zip(*buf):
        dic[a+b+c+d] += 1
print(*dic.values())