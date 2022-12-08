def solve():
    s = input()
    for l in range(len(s) - (len(s) & 1), 0, -2):
        for i in range(len(s) - l + 1):
            if sum(int(s[j]) for j in range(i, i + l // 2)) == sum(int(s[j]) for j in range(i + l // 2, i + l)):
                return l
    return 0
print(solve())