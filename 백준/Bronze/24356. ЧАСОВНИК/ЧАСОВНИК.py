a,b,c,d=map(int,input().split())
print(t:=(d-b+(c-a)*60)%1440,t//30)