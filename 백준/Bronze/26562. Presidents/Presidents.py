dic = {'Franklin': 100, 'Grant': 50, 'Jackson': 20, 'Hamilton': 10, 'Lincoln': 5, 'Washington': 1}
for _ in range(int(input())):
    money = sum(dic[name] for name in input().split())
    print('$', money, sep='')