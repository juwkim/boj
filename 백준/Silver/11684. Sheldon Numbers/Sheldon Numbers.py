X, Y = map(int, input().split())
ans = set()
for N in range(1, 64):
    for M in range(1, 63):
        pattern_1 = '1' * N
        pattern_0 = '0' * M
        s = ''
        toggle = True
        while True:
            if toggle:
                s += pattern_1
            else:
                s += pattern_0
            toggle ^= 1
            num = int(s, 2)
            if num > Y:
                break
            if num >= X:
                ans.add(num)
print(len(ans))