import sys
input = lambda: sys.stdin.readline().rstrip()

while (s:=input()) != '0':
    n, *nums = s.split()
    n = int(n[:-1])
    nums = [*map(int, nums)]
    d = {num: i for i, num in enumerate(nums)}
    ans = "yes"
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            k = 2 * nums[j] - nums[i]
            if 0 <= k < n and d[k] > j:
                ans = "no"
                break
        if ans == "no":
            break
    print(ans)