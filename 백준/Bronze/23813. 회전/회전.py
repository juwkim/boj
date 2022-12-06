N=input()
print(sum(int(N[i:]+N[:i])for i in range(len(N))))