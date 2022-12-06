n = int(input())
s = input()
       
ans = 0
one, two = 0, 0
for c in s:
    if c == '1':
        if one + 2 * two < n:
            one += 1
        elif two:
            two -= 1
            one += 1
    elif one + 2 * two < n-1:
        two += 1
    ans += one + two
print(ans)