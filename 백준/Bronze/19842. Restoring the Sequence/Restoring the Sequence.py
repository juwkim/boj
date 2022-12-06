n = int(input())
flag = 0
if n - 1 == int(input()):
    s = [*map(int, input().split())]
    if s == sorted(s) and len(k := {*range(1,n+1)} - {*s}) == 1:
        flag = 1
print(f'Yes {[*k][0]}' if flag else 'No')