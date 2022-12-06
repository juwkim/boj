d={'e':-30,'x':0,'c':0}
exec('s,n=input().split();d[s[1]]+=int(n);'*int(input()))
print(['not ',''][(d['e'] > 7) * (d['x'] > 13) * (d['c'] > 8)]+'liveable')