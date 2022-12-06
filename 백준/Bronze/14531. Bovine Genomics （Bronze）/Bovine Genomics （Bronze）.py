g=lambda x:[*map(set,zip(*[input()for _ in range(x)]))]
N=int(input().split()[0])
print(sum(x&y==set()for x,y in zip(g(N),g(N))))