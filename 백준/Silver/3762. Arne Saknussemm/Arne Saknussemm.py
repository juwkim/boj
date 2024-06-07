s = open(0).read().split()
i = 0
while i < len(s):
    n, k = int(s[i]), len(s[i + 1])
    ans = []
    for y in range(k - 1, -1, -1):
        for x in range(i + n, i, -1):
            if s[x][y] == '_':
                ans.append(' ')
            elif s[x][y] == '\\':
                ans.append('\n')
            else:
                ans.append(s[x][y])
    print("".join(ans).rstrip(), sep='')
    print()
    i += n + 1