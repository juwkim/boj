g = lambda: [*map(int, input().split())]


N = int(input())
nums = g()

a, b = nums[0], nums[-1]
for i in range(N-3):
    if a > b:
        a -= 1
    else:
        b -= 1
print(max(a, b) - 1)