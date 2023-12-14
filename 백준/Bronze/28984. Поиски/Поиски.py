s = input()
x = int(input())
L = s.count('L')
R = len(s) - L

ans = 'NO'
if L and R:
    ans = 'YES'
elif L:
    if x <= -L:
        ans = 'YES'
elif R:
    if x >= R:
        ans = 'YES'
print(ans)