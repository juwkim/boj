from collections import*
c=Counter(open(0)).values()
print(1-sum(V*V for V in c)/sum(c)**2)