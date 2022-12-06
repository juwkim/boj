for _ in range(int(input())):
    k = sum(map(lambda s: ord(s) - 64, input().replace(' ', '')))
    print('PERFECT LIFE' if k == 100 else k)