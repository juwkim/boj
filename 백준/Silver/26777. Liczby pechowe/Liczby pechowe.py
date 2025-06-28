from functools import lru_cache

N = input()
length = len(N)
digits = list(map(int, N))

@lru_cache(maxsize=None)
def dp(pos, sum_digits, tight, has13, prev_digit):
    if pos == length:
        return has13 and sum_digits == 13
    limit = digits[pos] if tight else 9
    return sum(dp(pos + 1, sum_digits + d, tight and d == limit, has13 or (prev_digit == 1 and d == 3), d) for d in range(limit + 1))
print(dp(0, 0, True, False, -1))