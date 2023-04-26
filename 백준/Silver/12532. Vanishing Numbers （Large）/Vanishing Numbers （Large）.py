from fractions import Fraction

for i in range(int(input())):
    print(f'Case #{i+1}:')
    l = sorted([f:=input(), f:= Fraction(f), set()] for i in range(int(input())))
    E = []
    while l:
        L = []
        x = []
        for i, j, k in l:
            if j in k:
                E.append(i)
            elif j < Fraction(1, 3):
                k.add(j)
                L.append((i, j * 3, k))
            elif j > Fraction(2, 3):
                k.add(j)
                L.append((i, (1 - j) * 3, k))
            else:
                x.append(i)
        for i in sorted(x):
            print(i)
        l = L
    for i in sorted(E):
        print(i)