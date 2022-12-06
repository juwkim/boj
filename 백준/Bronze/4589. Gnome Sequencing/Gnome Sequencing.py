print('Gnomes:')
for i in range(int(input())):
    s = [*map(int, input().split())]
    print('Ordered' if s in [sorted(s), sorted(s, reverse=True)] else 'Unordered')