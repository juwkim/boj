from itertools import combinations

ans = "Sequence is 3-free."
n, *nums = map(int, input().split())
s = {*nums}
for a, b in combinations(sorted(nums), 2):
    c = 2 * b - a
    if c in s:
        ans = f"Sequence is not 3-free. Witness: {a},{b},{c}."
        break
print(ans)