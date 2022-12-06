S = int(input())
a = [[int(t), int(t-1)] for K in range(1, S) if (t:=(S+K)/(2*K)) == int(t)]
b = [[int(t), int(t-1)] for K in range(2, S) if (t:=(S+K-1)/(2*K-1)) == int(t)]
c = [[int(t)]*2 for K in range(2, S) if (t:=S/K) == int(t)]
print(f'{S}:', *map(lambda x: ','.join(map(str, x)), sorted([*a, *b, *c])), sep='\n')