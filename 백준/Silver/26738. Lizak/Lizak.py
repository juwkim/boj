from collections import defaultdict

N, *A = map(int, open(0).read().split())
pos = defaultdict(list)
for idx, taste in enumerate(A):
    pos[taste].append(idx)
res = N + 1
for indices in pos.values():
    for i in range(len(indices) - 2):
        res = min(res, indices[i + 2] - indices[i] + 1)
if res == N + 1:
    print("NIE")
else:
    print(res)