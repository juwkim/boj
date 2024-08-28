import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]

l, r = 0, n - 1
sum_l, sum_r = a[0], a[n - 1]
ans_l, ans_r = l, r
ans = abs(sum_l - sum_r)
while l < r - 1:
    if sum_l < sum_r:
        l += 1
        sum_l += a[l]
    else:
        r -= 1
        sum_r += a[r]
    if ans > abs(sum_l - sum_r):
        ans_l, ans_r = l, r
        ans = abs(sum_l - sum_r)
print(ans, ans_l + 1, ans_r + 1)