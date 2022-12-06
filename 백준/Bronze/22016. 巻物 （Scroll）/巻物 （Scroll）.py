K,T=int(input().split()[1])-1,input()
print(T[:K],end='')
for i in T[K:]:print(chr(ord(i)^32),end='')