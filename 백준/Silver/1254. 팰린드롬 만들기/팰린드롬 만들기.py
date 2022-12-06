s = input()
l = len(s)
if s == s[::-1]:
    print(l)
else:
    for i in range(1, l):
        if s[i:] == s[:i-1:-1]:
            print(l + i)
            break