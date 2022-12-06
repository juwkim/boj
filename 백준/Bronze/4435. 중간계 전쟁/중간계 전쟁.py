s = [1, 2, 3, 3, 4, 10]
t = [1, 2, 2, 2, 3, 5, 10]
words = ['No victor on this battle field', 'Good triumphs over Evil', 'Evil eradicates all trace of Good'] 
g = lambda a: sum(a[i] * x for i,x in enumerate(map(int, input().split())))
for i in range(int(input())):
    gan, sau = g(s), g(t)
    print(f'Battle {i+1}: {words[(gan > sau) - (gan < sau)]}')