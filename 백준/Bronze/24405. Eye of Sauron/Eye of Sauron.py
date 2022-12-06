s=input()
n=len(s)//2-1
print(['fix','correct'][s=='|'*n+'()'+'|'*n])