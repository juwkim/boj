import sys
input = lambda: sys.stdin.readline().strip()
g = lambda: [*map(int, input().split())]
from itertools import product

while (name:=input()) != '#':
    state = [[0] * 5 for _ in range(6)]
    for i, num in enumerate(g()):
        state[i + 1][i] = num
    print(name)
    print("URN        R      O      Y      G      B")
    while (l:=g()) != [0, 0, 0]:
        num, src, dest = l
        total = sum(state[src])
        if total == 0:
            continue
        if total <= num:
            for i in range(5):
                state[dest][i] += state[src][i]
            state[src] = [0, 0, 0, 0, 0]
        else:
            nums = [num * state[src][i] / total for i in range(5)]
            cnt, discrepancy = None, 5
            for l in product((0, 1), repeat=5):
                cur = [int(nums[i]) + l[i] for i in range(5)]
                cur_discrepancy = sum(abs(a - b) for a, b in zip(cur, nums))
                if cur_discrepancy < discrepancy:
                    cnt, discrepancy = cur, cur_discrepancy
            for i in range(5):
                state[src][i] -= cnt[i]
                state[dest][i] += cnt[i]

    for i in range(1, 6):
        a, b, c, d, e = state[i]
        print(f"{i}    {a:7}{b:7}{c:7}{d:7}{e:7}")
    print()