import sys
branchorama = [list(map(int, tree.split())) for tree in sys.stdin.read().split('\n')]
for tree in branchorama:
    if tree == [0]:
        break
    leaf = 1
    for i in range(1, tree[0] + 1):
        leaf = leaf * tree[i * 2 - 1] - tree[i * 2]
    print(leaf)