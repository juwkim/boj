for _ in' '*int(input()):
 b=bin(int(input()))
 n=int(b[3:],2)+1
 for f in range(len(b)-2,0,-1):
  print(f"{f}{n:018d}")
  n=(n+1)//2