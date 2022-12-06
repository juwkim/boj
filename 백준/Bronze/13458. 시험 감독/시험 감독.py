g = lambda: map(int, input().split())
N = int(input())
A = [*g()]
B, C = g()
print(N + sum(max((i-B-1)//C + 1, 0) for i in A))