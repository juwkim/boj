g = lambda: [*map(int, input().split())]

C, n = g()
now = 0
o, i, s = g()
flag = 'possible'
if o == 0 and ((i < C and s == 0) or (i == C)):
    now = i
    for _ in range(n-2):
        o, i, s = g()
        tmp = now - o + i
        if o > now or tmp > C or (tmp < C and s):
            flag = 'impossible'
            break
        now = tmp
    o, i, s = g()
    if o != now or i or s:
        flag = 'impossible'
else:
    flag = 'impossible'
print(flag)