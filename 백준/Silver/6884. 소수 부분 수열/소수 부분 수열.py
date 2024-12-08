import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n, *nums = map(int, input().split())
    px = [0] * (n + 1)
    for i in range(n):
        px[i + 1] = px[i] + nums[i]
    ans = "This sequence is anti-primed."
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            if is_prime(px[i + l] - px[i]):
                ans = f"Shortest primed subsequence is length {l}: {' '.join(map(str, nums[i:i + l]))}"
                break
        else:
            continue
        break    
    print(ans)