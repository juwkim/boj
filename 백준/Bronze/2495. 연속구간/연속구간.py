for _ in[0]*3:
    s,t,n=input(),1,1
    for x,y in zip(s,s[1:]):
        if x==y:n+=1
        else:t,n=max(t,n),1
    print(max(t,n))