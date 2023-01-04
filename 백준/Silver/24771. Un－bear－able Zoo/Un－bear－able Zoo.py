from collections import defaultdict
cnt = 1
while N:= int(input()):
    dic = defaultdict(int)
    for _ in range(N):
        dic[input().split()[-1].lower()] += 1
    print(f'List {cnt}:')
    for name, amount in sorted(dic.items()):
        print(f'{name} | {amount}')
    cnt += 1