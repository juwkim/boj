a, b, c = map(int, input().split())
x, y = divmod(a*b, c)
print('.'.join([str(x), str(y/c).replace('0.', '')]))