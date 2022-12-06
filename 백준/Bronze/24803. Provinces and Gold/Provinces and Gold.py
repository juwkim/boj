G,S,C=map(int,input().split())
p=G*3+S*2+C
s=['','Estate','Duchy','Province'][(p>1)+(p>4)+(p>7)]
t=['Copper','Silver','Gold'][(p>2)+(p>5)]
print(s+' or '+t if s else t)