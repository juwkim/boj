import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    t, s = input().split()
    if t == 'b':
        num = 0
        for c in s:
            num = -2 * num + (c == '1')
        print(f"From binary: {s} is {num}")
    else:
        num = int(s)
        bin_str = ''
        while True:
            bin_str = str(num & 1) + bin_str
            num = -(num >> 1)
            if num == 0:
                break
        print(f"From decimal: {s} is {bin_str}")