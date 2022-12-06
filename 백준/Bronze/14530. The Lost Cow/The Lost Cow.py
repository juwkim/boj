from math import log,ceil
t=eval(input().replace(' ','-'))
print(t-2+4**(ceil(log(t/2,4))+1)if t>0 else -t+2*(4**ceil(log(-t,4))-1)if t<0 else 0)