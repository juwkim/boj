for _ in range(int(input())):
    n = int(input())
    if n < 10:
        for _ in range(n):
            input()
        print('MOREPROBLEMS')
    else:
        res = [0] * 10
        for _ in range(n):
            b, d = map(int, input().split())
            res[d-1] = max(res[d-1], b)
        print(sum(res) if all(res) else 'MOREPROBLEMS')