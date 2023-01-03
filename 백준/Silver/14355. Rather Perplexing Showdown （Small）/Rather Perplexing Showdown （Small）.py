from itertools import permutations
def g(): return [*map(int, input().split())]

for t in range(1, 1 + int(input())):
    N, R, P, S = g()
    buf = ['P'] * P + ['R'] * R + ['S'] * S
    ans = None
    for l in permutations(buf, 1 << N):
        buf = l
        for i in range(N):
            new_buf = []
            for j in range(0, len(buf), 2):
                if buf[j] == buf[j+1]:
                    break
                if buf[j] + buf[j+1] in ('PR', 'RS', 'SP'):
                    new_buf.append(buf[j])
                else:
                    new_buf.append(buf[j+1])
            else:
                buf = new_buf
                continue
            break
        if len(buf) == 1:
            ans = ''.join(l)
            break
    if ans:
        print(f'Case #{t}: {ans}')
    else:
        print(f'Case #{t}: IMPOSSIBLE')