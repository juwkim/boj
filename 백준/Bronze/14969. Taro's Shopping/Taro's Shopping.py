from itertools import combinations
while m:=int(input().split()[1]):
    k = [sum(i) for i in combinations(map(int, input().split()), 2) if sum(i) <= m]
    print(max(k) if k else 'NONE')