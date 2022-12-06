import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    m = int(input())
    words = [input().rstrip() for _ in range(m)]
    
    print(f'Scenario #{cnt}:')
    for _ in range(int(input())):
        pwd = [words[i] for i in g()[1:]]
        print(*pwd, sep='')
    print()