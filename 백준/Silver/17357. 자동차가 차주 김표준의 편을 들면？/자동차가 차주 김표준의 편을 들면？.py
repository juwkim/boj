g = lambda: tuple(map(int, input().split()))

def pvariance(arr):
    x_sum, x2_sum = 0, 0
    for num in arr:
        x_sum += num
        x2_sum += num * num
    n = len(arr)
    ret = x2_sum * n - x_sum ** 2
    return ret
    
N = int(input())
nums = [*map(int, input().split())]
for size in range(1, N + 1):
    i = max(range(N - size + 1), key=lambda x: (pvariance(nums[x:x+size]), -x))
    print(i + 1)