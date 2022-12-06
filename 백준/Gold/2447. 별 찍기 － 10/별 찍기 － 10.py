N,S=int(input()),'*'
while N>1:S=(k:=[c*3 for c in S])+[c+' '*len(c)+c for c in S]+k;N//=3
print(*S)