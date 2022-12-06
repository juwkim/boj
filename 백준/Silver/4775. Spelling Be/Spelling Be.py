import sys
input = lambda: sys.stdin.readline().rstrip()

Set = {input() for _ in range(int(input()))}
for _ in range(1, 1 + int(input())):
    buf = []
    while (s:= input()) != '-1':
        if s not in Set:
            buf.append(s)
    
    if buf:
        print(f'Email {_} is not spelled correctly.')
        for word in buf:
            print(word)
    else:
        print(f'Email {_} is spelled correctly.')
print('End of Output')