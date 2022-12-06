while True:
    nums = [*map(int, input().split())]
    if nums == [0]:
        break
    N, P = nums
    a = 3 - P + (P - 1)//2 * 4
    b, c = 1 + N - P, 1 + N - a
    print(*sorted([a, b, c]))