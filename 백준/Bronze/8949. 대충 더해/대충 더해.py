a, b = input().split()
a, b = map(lambda s: s.zfill(max(len(a), len(b))), [a, b])
print(''.join(map(str,[sum(map(int,x))for x in zip(a, b)])))