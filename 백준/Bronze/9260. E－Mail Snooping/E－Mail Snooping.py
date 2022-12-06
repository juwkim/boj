g = lambda: [*map(int, input().split())]


for cnt in range(1, 1 + int(input())):
    n, k, t = g()
    words = {input() for _ in range(n)}
    for _ in range(k):
        tmp = input().replace(',', ' ').replace('.', ' ')
        words -= set(tmp.split())
    print(f'Data Set {cnt}:')
    if len(words) <= n - t:
        print('Alarm\n')
    else:
        print('No Alarm\n')