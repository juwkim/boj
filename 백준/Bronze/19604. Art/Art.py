p = [[*map(int, input().split(','))] for _ in range(int(input()))]
print(f'{min(i[0]-1 for i in p)},{min(i[1]-1 for i in p)}')
print(f'{max(i[0]+1 for i in p)},{max(i[1]+1 for i in p)}')