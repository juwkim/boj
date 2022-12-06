import sys
input = sys.stdin.readline

buf = {*range(1, 11)}
while n:= int(input()):
    reply = input().rstrip()
    if reply[-1] == 'h':
        buf -= {*range(n, 11)}
    elif reply[-1] == 'w':
        buf -= {*range(1, n+1)}
    else:
        print('Stan may be honest' if n in buf else 'Stan is dishonest')
        buf = {*range(1, 11)}