import sys
input = lambda: sys.stdin.readline().rstrip()

t = input()
M, F = {}, {}
while (s:=input())[0] != '*':
    name, sex, gene = s.split()
    if sex == 'M':
        M[name] = gene
    else:
        F[name] = gene
mothers, fathers = sorted(F), sorted(M)
while (s:=input())[0] != '*':
    name, gene = s.split()
    ans = []
    for mother in mothers:
        for father in fathers:
            for RD, a, b, c in zip(t, F[mother], M[father], gene):
                if RD == 'D':
                    if (a, b) == ('0', '0'):
                        if c == '1':
                            break
                    elif c == '0':
                        break
                else:
                    if (a, b) == ('1', '1'):
                        if c == '0':
                            break
                    elif c == '1':
                        break
            else:
                ans.append(f"{mother}-{father}")
    print(f"{name} by {' or '.join(ans)}")