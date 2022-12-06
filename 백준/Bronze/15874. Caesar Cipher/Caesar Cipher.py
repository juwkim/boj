k=int(input().split()[0])
print(''.join(map(lambda i:chr((t:=65+32*i.islower())+(ord(i)+k-t)%26)if i.isalpha()else i,input())))