N = int(input())
nums = [*map(int, input().split())]
check = bytearray(N)
for i in range(N):
    if nums[i] == 0:
        continue
    if i and check[i - 1] == 0:
        check[i - 1] = 1
        nums[i] -= 1
    if nums[i] and check[i] == 0:
        check[i] = 1
        nums[i] -= 1
    if nums[i] and i + 1 < N:
        check[i + 1] = 1
        nums[i] -= 1
print(sum(check))