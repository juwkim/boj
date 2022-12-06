import itertools as i
_,s=input(),input()
t=[sum(x==y for x,y in zip(i.cycle(p),s))for p in['ABC','BABC','CCAABB']]
print(max(t),*[['Adrian','Bruno','Goran'][i]for i in range(len(t))if t[i]==max(t)])