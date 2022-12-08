m = input()
ans, Max = 'No Jam', 0
for _ in range(int(input())):
    w, g = input().split()
    
    i, j, num = 0, 0, 0
    while i < len(m) and j < len(w):
        if m[i] == w[j]:
            i += 1
        else:
            num += 1
        j += 1
    num += len(w) - j
    if i == len(m):
        if Max < int(g) / num:
            Max = int(g) / num
            ans = w
print(ans)