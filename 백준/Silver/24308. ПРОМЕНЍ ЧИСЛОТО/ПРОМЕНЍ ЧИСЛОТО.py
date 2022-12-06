N = [*input()]
ans = None
if N[0] in '-+':
    s = 1
else:
    s = 0
for i in range(s, len(N)-1):
    check1 = set(map(str, range(10)))
    check1.remove(N[i])
    if i == s:
        check1.remove('0')
    
    tmp1 = N[i]
    for a in check1:
        N[i] = a
        for j in range(i+1, len(N)):
            check2 = set(map(str, range(10)))
            check2.remove(N[j])
            tmp2 = N[j]
            for b in check2:
                N[j] = b
                num = int(''.join(N))
                if num % 6 == 0:
                    if ans == None:
                        ans = num
                    else:
                        ans = max(ans, num)
            N[j] = tmp2
    N[i] = tmp1
print(ans)