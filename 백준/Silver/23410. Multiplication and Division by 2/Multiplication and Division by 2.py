import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    if y == 0:
        print("Yes")
        continue
    while y % 2 == 0: y >>= 1
    ans = "No"
    s = bin(x)[2:]
    for i in range(len(s)):
        if s[i] == '0':
            continue
        num = 0
        for j in range(i, len(s)):
            num = (num << 1) + (s[j] == '1')
            if num == y:
                ans = "Yes"
                break
        if ans == "Yes":
            break
    print(ans)