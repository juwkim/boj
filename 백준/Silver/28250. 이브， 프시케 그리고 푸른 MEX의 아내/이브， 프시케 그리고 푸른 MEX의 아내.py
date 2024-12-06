N, *A = map(int, open(0).read().split())
zero, one, left = 0, 0, 0
for num in A:
    if num == 0:
        zero += 1
    elif num == 1:
        one += 1
    else:
        left += 1
print(zero * (zero - 1) // 2 + zero * (2 * one + left))