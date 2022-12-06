from math import factorial
from collections import Counter
while n:=int(input()):
    input(f'{n}! --\n')
    s = Counter(str(factorial(n)))
    print(f'{"(0)":>6}{s["0"]:>5}', end='')
    for i in range(1, 5):
        print(f'{"("+str(i)+")":>7}{s[str(i)]:>5}', end='')
    print(f'\n{"(5)":>6}{s["5"]:>5}', end='')
    for i in range(6, 10):
        print(f'{"("+str(i)+")":>7}{s[str(i)]:>5}', end='')
    print('')