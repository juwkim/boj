def solve(n, min_num):
    if mem[n][min_num] == 0:
        mem[n][min_num] = 1 + sum(solve(n - i, i) for i in range(min_num, n // 2 + 1))
    return mem[n][min_num]

mem = [[0] * 51 for _ in range(101)]
print(solve(int(input()), 5))