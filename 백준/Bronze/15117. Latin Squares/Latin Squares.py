g = lambda: [*map(int, input().split())]

n = int(input())
a = [[*input()] for _ in range(n)]
a += [*zip(*a)]
p = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]
test = {*p}
if all(set(i) == test for i in a):
    if ''.join(a[0]) + ''.join(a[n]) == p * 2:
        print('Reduced')
    else:
        print('Not Reduced')
else:
    print('No')