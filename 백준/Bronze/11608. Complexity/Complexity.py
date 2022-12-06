from collections import*
print(sum(sorted(Counter(input()).values())[:-2]))