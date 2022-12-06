T, min_num = map(int, [input(), input()])
total = 0
for _ in range(T-1):
    N = int(input())
    if N < min_num:
        min_num = N
    elif N > min_num:
        total += N - min_num
print(total)