n, p, h = map(int, input().split())
for _ in range(n):
    x = int(input())
    if x < p:
        print(f'NTV: Dollar dropped by {p-x} Oshloobs')
    p = x
    if x > h:
        print(f'BBTV: Dollar reached {x} Oshloobs, A record!')
        h = x