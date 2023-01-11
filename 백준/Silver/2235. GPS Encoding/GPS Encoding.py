def solve(buf, idx):
    global ans
    
    tmp = ''.join(buf)
    if ans and (-len(tmp), tmp) <= (-len(ans), ans):
        return

    if idx >= len(seq):
        ans = tmp
        return
    
    num = int(seq[idx:idx+2])
    if num < 26:
        solve(buf + [key[num]], idx + 2)
    solve(buf + [key[int(seq[idx])]], idx + 1)

t = 1
while (key:= input()) != '#':
    
    print(f'Problem {t}')
    while (seq:= input()) != '0':
        ans = None
        solve([], 0)
        print(ans)
    
    t += 1
    print()