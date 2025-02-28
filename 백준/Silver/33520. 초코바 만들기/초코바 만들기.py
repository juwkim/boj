a,b=zip(*[sorted(map(int,l.split()))for l in[*open(0)][1:]])
print(max(a)*max(b))