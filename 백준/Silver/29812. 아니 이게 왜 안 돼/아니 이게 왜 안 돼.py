input()
S=input()
D,M=map(int,input().split())
a=sum(min(D*len(l),M+D)for l in S.translate(str.maketrans("HYU","   ")).split())
b=min(S.count(i)for i in"HYU")
print(["Nalmeok",a][a>0])
print(["I love HanYang University",b][b>0])