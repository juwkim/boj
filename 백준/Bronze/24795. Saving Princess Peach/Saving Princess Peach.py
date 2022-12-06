N, Y = map(int, input().split())
find = {*[int(input()) for _ in range(Y)]}
left = {*range(N)} - find
if left:
    print(*sorted(left), sep='\n')
print(f'Mario got {len(find)} of the dangerous obstacles.')