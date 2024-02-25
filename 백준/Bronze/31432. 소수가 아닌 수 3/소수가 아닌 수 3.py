N, *_, D = open(0).read().split()
print("YES")
if D == '0':
    print(0)
else:
    print(D * 3)