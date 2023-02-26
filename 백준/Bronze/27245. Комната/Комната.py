w, l = sorted([int(input()), int(input())])
h = int(input())
if 2 * h <= w and l <= 2 * w:
    print('good')
else:
    print('bad')