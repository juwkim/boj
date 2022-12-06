s = input()
idx = s.find('x')
if idx == -1:
    print(0)
elif idx == 0:
    print(1)
elif s[:2] == '-x':
    print(-1)
else:
    print(s[:idx])