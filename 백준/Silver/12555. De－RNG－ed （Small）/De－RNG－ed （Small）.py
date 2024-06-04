import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0: return False
    return True

for tc in range(1, 1 + int(input())):
    D, K = g()
    nums = g()
    def solve():
        if K == 1 or (K == 2 and nums[0] != nums[1]):
            return "I don't know."
        if len(set(nums)) == 1:
            return nums[0]
        if K == 3:
            x, y, z = nums
            check = set()
            for P in range(max(nums) + 1, 10 ** D):
                if is_prime(P) and (y - x) % P:
                    A = (z - y) * pow(y - x, -1, P) % P
                    B = (y - A * x) % P
                    check.add((A * z + B) % P)
                    if len(check) > 1:
                        return "I don't know."
            return check.pop()
        x, y, z = nums[:3]
        check = set()
        for P in range(max(nums) + 1, 10 ** D):
            if is_prime(P) and (y - x) % P:
                A = (z - y) * pow(y - x, -1, P) % P
                B = (y - A * x) % P
                if all((A * nums[i] + B) % P == nums[i + 1] for i in range(2, K - 1)):
                    check.add((A * nums[-1] + B) % P)
                    if len(check) > 1:
                        return "I don't know."
        return check.pop()
    print(f"Case #{tc}: {solve()}")