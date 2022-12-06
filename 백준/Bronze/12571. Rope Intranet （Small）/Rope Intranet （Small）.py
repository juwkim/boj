for i in range(int(input())):
    w=[*zip(*sorted([*map(int,input().split())]for _ in[0]*int(input())))][1]
    c=sum(sum(w[j]>s for s in w[j+1:])for j in range(len(w)-1))
    print(f'Case #{i+1}: {c}')