for _ in range(int(input())):
    N = int(input())
    nums = [0] + [int(input()) for _ in range(N)]
    cur, K = 1, 0
    check = set([1])
    while True:
        K += 1
        cur = nums[cur]
        if cur == N:
            break
        if cur in check:
            K = 0
            break
        check.add(cur)
    print(K)