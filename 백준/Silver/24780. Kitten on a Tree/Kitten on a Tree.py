import sys
input = sys.stdin.readline

cur = int(input())
tree = [0] * 101
while True:
    a, *bs = map(int, input().split())
    if a == -1:
        break
    for b in bs:
        tree[b] = a
while cur:
    print(cur, end=' ')
    cur = tree[cur]