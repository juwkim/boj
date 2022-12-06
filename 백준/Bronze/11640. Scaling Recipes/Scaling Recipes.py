g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    
    R, P, D = g()
    ingre = [input().split() for _ in range(R)]
    max_ingre = float(list(filter(lambda x: x[2] == '100.0', ingre))[0][1]) * D / P
    
    print(f'Recipe # {_}')
    for name, amount, percentage in ingre:
        print(name, "%.1f" % (max_ingre * float(percentage) / 100))
    print('----------------------------------------')