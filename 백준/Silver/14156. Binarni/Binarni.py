N=int(input())
for i in range(1<<N):print(format(i^i>>1,f'0{N}b'))