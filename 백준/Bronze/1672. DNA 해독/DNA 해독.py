change = {'AA': 'A', 'AG': 'C', 'AC': 'A', 'AT': 'G',
     'GA': 'C', 'GG': 'G', 'GC': 'T', 'GT': 'A',
     'CA': 'A', 'CG': 'T', 'CC': 'C', 'CT': 'G',
     'TA': 'G', 'TG': 'A', 'TC': 'G', 'TT': 'T'}

N, S = int(input()), input()
if len(S) == 1:
    print(S)
else:
    A_n_1, A_n = S[-2], S[-1]
    for i in range(-3, -N-1, -1):
        A_n_1, A_n = S[i], change[A_n_1 + A_n] 
    print(change[A_n_1 + A_n])