n,m=map(int,input().split())
print(sum(len(s:=input())==len(set(s))and 65+m>ord(max(s))for _ in[0]*n))