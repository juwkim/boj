buf = [[('.', 'O'), ('P', '.')],
       [('I', '.'), ('.', 'P')],
       [('O', '.'), ('.', 'P')]]
ans = 3
txt = ('T', 'F', 'Lz', '?')
c = "SWNE".index(input())
jump = [tuple(input()), tuple(input())]
for i in range(3):
    for _ in range(c):
        buf[i] = [l[::-1] for l in zip(*buf[i])]
    if jump == buf[i]:
        ans = i
        break
print(txt[ans])