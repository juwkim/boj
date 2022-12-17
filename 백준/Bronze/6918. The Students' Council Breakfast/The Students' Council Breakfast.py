a, b, c, d = [int(input()) for _ in range(4)]
p = int(input())
ans, total = 1e9, 0
for i in range(p // a + 1):
    x = p - a * i
    for j in range(x // b + 1):
        y = x - b * j
        for k in range(y // c + 1):
            z = y - c * k
            l, q = divmod(z, d)
            if q == 0:
                print(f'# of PINK is {i} # of GREEN is {j} # of RED is {k} # of ORANGE is {l}')
                ans = min(ans, i + j + k + l)
                total += 1
print(f'Total combinations is {total}.')
print(f'Minimum number of tickets to print is {ans}.')