N = int(input())
isodd = input()[0] == 'a'
K = int(input())
if K&1 == isodd:
    print(K)
elif K + 1 <= N:
    print(K + 1)
else:
    print(K - 1)