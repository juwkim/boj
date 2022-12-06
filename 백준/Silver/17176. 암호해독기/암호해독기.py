g = lambda: [*map(int, input().split())]

alpha = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
N = int(input())
s = sorted(alpha[num] for num in g())
pwd = sorted(input())
if s == pwd:
    print('y')
else:
    print('n')