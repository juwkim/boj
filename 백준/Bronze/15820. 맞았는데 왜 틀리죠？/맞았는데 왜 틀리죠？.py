S1, S2 = map(int, input().split())
if all(len(set(input().split())) == 1 for _ in range(S1)):
    if all(len(set(input().split())) == 1 for _ in range(S2)):
        print('Accepted')
    else:
        print('Why Wrong!!!')
else:
    print('Wrong Answer')