g=lambda:map(int, input().split())
input()
print(sum(abs(a-b)for a,b in zip(g(),g()))//2)