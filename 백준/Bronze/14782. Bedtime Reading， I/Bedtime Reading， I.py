n = int(input())
print(sum(filter(lambda x: n%x == 0, range(1, n+1))))