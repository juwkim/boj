from itertools import permutations

N, d = map(int, input().split())
if N * (d - 1) ** 2 >= d + (d - 2) * d ** (d + 1):
    print(-1)
else:
    for s in permutations(range(d), d):
        if s[0] == 0:
            continue
        num = int("".join(map(str, s)), d)
        if num > N:
            print(num)
            break