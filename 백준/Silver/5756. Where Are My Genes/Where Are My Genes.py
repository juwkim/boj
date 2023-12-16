import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

tc = 1
while N:=int(input()):
    gene = [*range(N + 1)]
    for _ in range(int(input())):
        i, j = g()
        gene[i:j+1] = gene[i:j+1][::-1]
    print(f"Genome {tc}")
    for _ in range(int(input())):
        print(gene.index(int(input())))
    tc += 1