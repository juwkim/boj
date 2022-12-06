g = lambda x: '(' * (int(x) < 0) + str(x) + ')' * (int(x) < 0)
s = ' '.join(map(g, input().split()))
operation = [s.replace(' ', '+-*'[i]) for i in range(3)]
num = [eval(i) for i in operation]
if num.count(max(num)) == 1:
    k = num.index(max(num))
    print(f'{operation[k]}={g(max(num))}')
else:
    print('NIE')