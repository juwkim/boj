from random import shuffle
import sys
input = lambda: sys.stdin.readline()

for t in range(1, 1 + int(input())):
    input()
    txt_list = input().split()
    if any(len(txt) == 1 for txt in txt_list):
        ans = 'IMPOSSIBLE'
    else:
        buf = [*map(chr, range(65, 91))]
        ans = ''.join(buf)
        while any(txt in ans for txt in txt_list):
            shuffle(buf)
            ans = ''.join(buf)
    print(f'Case #{t}: {ans}')