n=int(input())
s=input()
print(len(b:=[i for i in range(n-1)if s[i]!=s[i+1]]+[n-1])//2)
for i in range(0,len(b)-1,2):print(f"{b[i]+2}-{b[i+1]+1}")