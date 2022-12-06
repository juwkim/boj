r=input
for i in range(int(r())):S,F=r(),r();print(f'Case #{i+1}:',sum(min(map(lambda x:min(abs(ord(x)-ord(i)),26-abs(ord(x)-ord(i))),F))for i in S))