N= int(input())
K,S='@'*N,' '*N
p=(K+S*3+K+'\n')*N
print(p+(p+(K*5+'\n')*N)*2)