_, s = input(), input()
A, B = s.count('A'), s.count('B')
print(['Tie', 'A', 'B'][(A>B) - (A<B)])