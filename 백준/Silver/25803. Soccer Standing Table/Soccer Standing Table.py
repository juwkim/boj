from itertools import permutations

for mp, w, d, l, pts in permutations(map(int, input().split()), 5):
    if mp == w + d + l and w * 3 + d == pts:
        print(mp, w, d, l, pts)
        break