s = input()

cur = 0
idx = 0
while idx < len(s):
    while s[idx] not in '+-':
        idx += 1
    t = s[cur:idx]
    cmd = {'+': 'tighten', '-': 'loosen'}[s[idx]]
    
    idx += 1
    cur = idx
    while idx < len(s) and s[idx].isnumeric():
        idx += 1
    num = s[cur:idx]
    cur = idx
    
    print(t, cmd, num)