nums = [*map(int, input().split())]
ans = 0
def solve(i, a, b, score):
    global ans
    if i == 10:
        ans += score >= 5
        return
    for num in range(1, 6):
        if num == a == b:
            continue
        solve(i + 1, b, num, score + (nums[i] == num))
solve(0, 0, 0, 0)
print(ans)