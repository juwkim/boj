l, r = input(), input()
if len(l) == len(r):
    i = 0
    while i < len(r) and l[i] == r[i]:
        i += 1
    print(len(r) - i)
else:
    print(len(r))