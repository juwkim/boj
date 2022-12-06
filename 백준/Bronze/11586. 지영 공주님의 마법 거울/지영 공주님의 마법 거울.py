mirror = [input() for _ in range(int(input()))]
N = int(input())
if N == 1:
    print(*mirror, sep='\n')
elif N == 2:
    print(*[i[::-1] for i in mirror], sep='\n')
else:
    print(*mirror[::-1], sep='\n')