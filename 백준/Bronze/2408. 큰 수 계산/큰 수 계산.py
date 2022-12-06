N=int(input())
print(eval(''.join([input() for _ in [0]*(2*N-1)]).replace('/','//')))