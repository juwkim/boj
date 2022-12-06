import sys
for _ in[0]*int(input()):
    a=eval(sys.stdin.readline().replace(' ', '+'))
    print((a-1)*a**2//2)