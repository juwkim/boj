x = int(s:=input())
k = int(input())
if len(s) == 1:
    ans = x
elif k:
    c = 0
    while int(s[0] + str(c) * (len(s) - 1)) < x:
        c += 1
    ans = int(s[0] + str(c) * (len(s) - 1))
    for i in range(1, len(s)):
        c = 0
        while int(s[0] * i + str(c) + s[0] * (len(s) - i - 1)) < x:
            c += 1
        if c <= 9:
            ans = min(ans, int(s[0] * i + str(c) + s[0] * (len(s) - i - 1)))
elif s[0] == max(s):
    ans = s[0] * len(s)
else:
    ans = str(int(s[0]) + 1) * len(s)
print(ans)