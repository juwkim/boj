A, B, *nums = map(int, open(0).read().split())
P, Q = nums[:A], nums[A:]
def solve():
    ans = 0
    for start in range(B):
        i, j = 0, start
        while j < B:
            while i < A and P[i] != Q[j]:
                i += 1
            if i == A:
                break
            i += 1
            j += 1
        ans = max(ans, j - start)
    return ans
print(solve())