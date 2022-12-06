g = lambda: map(int, input().split())
K, L = g()
dic = {}
for i in range(L):
    dic[input()] = i
print(*[num for num in sorted(dic, key=lambda x: dic[x])[:K]])