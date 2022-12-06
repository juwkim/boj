n, d = input().split()
n = int(n)
if n < len(d):
    print('No solution')
else:
    print(d.ljust(n, '0'))