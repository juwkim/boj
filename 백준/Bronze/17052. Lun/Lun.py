n, card = int(input()), input()
s = [int(i) for i in card if '0' <= i <= '9']
x = card.index('x')
s.insert(x, 0)

if x == n - 1:
    for i in range(-2, -n -1, -2):
        s[i] = sum(divmod(2*s[i], 10))
    print(sum(s) * 9 % 10)

else:
    for i in range(-2, -n -1, -2):
        s[i] = sum(divmod(2*s[i], 10))
    a = sum(s[:-1])
    
    if x - n in range(-2, -n -1, -2):
        for i in range(10):
            if sum([a, *divmod(2*i, 10)]) * 9 % 10 == s[-1]:
                print(i)
                break
    else:
        for i in range(10):
            if sum([a, *divmod(i, 10)]) * 9 % 10 == s[-1]:
                print(i)
                break