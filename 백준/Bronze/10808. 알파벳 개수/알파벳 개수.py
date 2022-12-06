k={chr(i):0 for i in range(97,123)}
for a in input():
    k[a]+=1
print(*k.values())