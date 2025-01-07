import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    G, C, W = input().split()
    l.append((G, int(C), int(W)))
ans = "NONE"
for num in map(str, range(1000, 10000)):
    for G, C, W in l:
        c, w = 0, 0
        match = bytearray(4)
        for i in range(4):
            if num[i] == G[i]:
                c += 1
                match[i] = 1
        for i in range(4):
            if match[i]: continue
            for j in range(4):
                if match[j]: continue
                if num[i] == G[j]:
                    w += 1
                    match[j] = 1
                    break
        if c != C or w != W:
            break
    else:
        ans = num
        break
print(ans)