f = lambda l: sum(l[i-1] != l[i] for i in range(n))
n = int(input())
s = f(input())
print(("no", "yes")[s and s - (0, 2)[s == n] >= f(input())])