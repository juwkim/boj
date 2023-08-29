def solve():
    x1, x2, n = map(int, input().split())
    diff = x1 - x2

    if diff < 0:
        return "NO"
    if diff == 0:
        return ["NO", "YES"][n == 0]
    q, r = divmod(diff, 2)
    if n and q >= n and r == 0:
        return "YES"
    return "NO" 

print(solve())