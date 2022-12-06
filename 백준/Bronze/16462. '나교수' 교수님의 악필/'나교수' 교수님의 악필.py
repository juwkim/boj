import statistics as s
t=s.mean(min(100,int(''.join(map(lambda s:'9'if s in'06'else s,i))))for i in[input()for _ in[0]*int(input())])
t=int(t)+(t%1>=0.5)
print(t)