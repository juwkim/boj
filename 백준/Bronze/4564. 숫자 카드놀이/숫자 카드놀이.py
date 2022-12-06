from functools import reduce
while (S:=int(input())):
    print(S, end=' ')
    while S//10:
        S = reduce(lambda x, y: x*int(y), str(S), 1)
        print(S, end=' ')
    print('')