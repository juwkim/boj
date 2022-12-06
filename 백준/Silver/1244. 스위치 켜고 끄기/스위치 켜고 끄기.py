g = lambda: [*map(int, input().split())]

N = int(input())
buf = g()

for _ in range(int(input())):
    sex, num = g()
    if sex == 1:
        for i in range(num - 1, N, num):
            buf[i] ^= 1
    else:
        buf[num-1] ^= 1
        
        l, r = num - 2, num
        while l >= 0 and r < N and buf[l] == buf[r]:
            buf[l] ^= 1
            buf[r] ^= 1
            l -= 1
            r += 1
for i in range(0, N, 20):
    print(*buf[i:i+20])