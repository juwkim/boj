g = lambda: [*map(int, input().split())]

buf = []
for s in range(256):    
    ans = s & 1
    x = s & 1
    for j in range(1, 8):
        x = ((s & (1 << j)) >> j) ^ x
        ans += x << j       
    buf.append(ans)

N = int(input())
for num in g():
    print(buf[num], end=' ')