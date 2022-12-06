for i in range(1, 1+int(input())):
    r, c, w, h = map(int, input().split())
    head = ('+' + '-' * w) * c + '+'
    mid = ('|' + '*' * w) * c + '|'
    print(f'Case #{i}:\n{head}')
    for _ in range(r):
        print('\n'.join([mid for _ in range(h)]))
        print(head)