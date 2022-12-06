from collections import*
print(max(0,sum(i&1 for i in Counter(input()).values())-1))