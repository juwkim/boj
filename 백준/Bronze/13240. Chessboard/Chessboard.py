N, M = map(int, input().split())
star1 = M//2 * '*.' + M%2 * '*'
star2 = M//2 * '.*' + M%2 * '.'
for i in range(N//2):
    print(star1, star2, sep='\n')
for _ in range(N%2):
    print(star1)