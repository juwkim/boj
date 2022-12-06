N = int(input())
num = [*map(int, input().split())]
print(min([abs(num[i+1]-num[i]) for i in range(N-1)]))