from itertools import*
S=input()
a={"".join((s[0],*t,*s[1:]))for s,t in product(permutations(S[0]+S[4:]), permutations(S[1:4]))}
print(len(a))
print(*a,sep="\n")