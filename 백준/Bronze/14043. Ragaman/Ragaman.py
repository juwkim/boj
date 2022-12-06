from collections import Counter as C
a=C(input())
b=C(input())-a
print('NA'[len(b)==0 or (len(b)==1 and b['*']>0)])