input()
s=input().split()
try:print(1+max((s[i],i)for i in range(len(s))if s.count(s[i])==1)[1])
except:print('none')