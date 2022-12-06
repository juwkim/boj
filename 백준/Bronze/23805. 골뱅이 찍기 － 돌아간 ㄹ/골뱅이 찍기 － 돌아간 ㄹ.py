N=int(input())
K,S,a='@'*N,' '*N,'\n'
print((K*3+S+K+a)*N+(K+S+K+S+K+a)*3*N+(K+S+K*3+a)*N)