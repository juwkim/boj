n = int(input())
s = input()
t = input()
runs, in_run = 0, False
for i in range(n):
    if s[i] != t[i]:
        if not in_run:
            runs += 1
            in_run = True
    else:
        in_run = False
if runs:
    print(max(1, 2 * runs - (s[0] != t[0]) - (s[-1] != t[-1])))
else:
    print(0)