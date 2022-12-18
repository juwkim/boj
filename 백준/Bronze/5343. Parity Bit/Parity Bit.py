for _ in range(int(input())):
    s = input()
    ans = 0
    for i in range(0, len(s), 8):
        ans += s[i:i+8].count('1') & 1
    print(ans)