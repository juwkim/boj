w, o, l, f = 0, 0, 0, 0
ans = 1
prev = 'f'
for c in input():
    match c:
        case 'w':
            if prev in 'ol' or (prev == 'f' and l != f):
                ans = 0
                break
            w += 1
        case 'o':
            if prev in 'lf' or (prev == 'w' and w == f):
                ans = 0
                break
            o += 1
        case 'l':
            if prev in 'wf' or (prev == 'o' and w != o):
                ans = 0
                break
            l += 1
        case 'f':
            if prev in 'wo' or (prev == 'l' and o != l):
                ans = 0
                break
            f += 1
    prev = c
if not (w == o == l == f):
    ans = 0
print(ans)