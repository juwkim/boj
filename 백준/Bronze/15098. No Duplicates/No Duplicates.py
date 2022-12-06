from collections import*
print('yneos'[max(Counter(input().split()).values())!=1::2])