names = [input() for _ in range(int(input()))]
if names == sorted(names):
    print('INCREASING')
elif names == sorted(names, reverse=True):
    print('DECREASING')
else:
    print('NEITHER')