m,l=sum(map(o:=ord,S:=input())),len(S)>>1
print(*[chr(65+(o(S[i])+o(S[i+l])+m)%26)for i in range(l)],sep='')