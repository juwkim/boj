s=input()
print('yneos'[sum(s[i] in['qwertasdfgzxcvb','yuiophjklnm'][i&1]for i in range(len(s)))%len(s)!=0::2])