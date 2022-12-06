import sys
input = lambda: sys.stdin.readline().rstrip()

line = " ABCDEFGHIJKLMNOPQRSTUVWXYZ',-.?"
while (s:= input()) != '#':
    ans = []    
    num = []
    while True:
        
        now = 0
        for c in s:
            if c == ' ':
                now += 1
            elif now:
                num.append('10'[now&1])
                now = 0
        if now:
            num.append('10'[now&1])
        s = input()
        if s == '*':
            break
    for i in range(0, len(num), 5):
        c = int(''.join(num[i:i+5]).ljust(5, '0'), 2)
        ans.append(line[c])
    print(*ans, sep='')