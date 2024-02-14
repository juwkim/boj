import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
def point_sum(idx):
    res = 0
    while idx:
        res += tree[idx]
        res %= MOD
        idx -= idx & -idx
    return res

def range_sum(s, e):
    return (point_sum(e) - point_sum(s - 1)) % MOD

def update(idx, num):
    while idx <= N:
        tree[idx] += num
        tree[idx] %= MOD
        idx += idx & -idx

for tc in range(1, 1 + int(input())):
    n, m, X, Y, Z = map(int, input().split())
    A = [int(input()) for _ in range(m)]
    nums = []
    for i in range(n):
        nums.append(A[i % m])
        A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z
    dic = {num: i for i, num in enumerate(sorted(set(nums)), 1)}
    N = len(dic)
    tree = [0] * (N + 1)
    for num in map(dic.get, nums):
        update(num, 1 + range_sum(1, num - 1))
    ans = range_sum(1, N)
    print(f"Case #{tc}: {ans}")