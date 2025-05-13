n, *a = map(int, open(0).read().split())
blocks = []
prv = -1
for cur in a:
    if cur != prv:
        if prv != -1:
            blocks.append(prv)
        prv = cur
blocks.append(prv)
cnt = {color: len(blocks) for color in set(blocks)}
for i in range(len(blocks)):
    if i == 0 or i == len(blocks) - 1 or blocks[i - 1] != blocks[i + 1]:
        cnt[blocks[i]] -= 1
    else:
        cnt[blocks[i]] -= 2
idx = max(cnt, key=lambda x: cnt[x])
print(cnt[idx], idx)