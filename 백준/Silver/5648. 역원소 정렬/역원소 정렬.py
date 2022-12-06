n, *l = open(0).read().split()
print(*sorted(int(num[::-1]) for num in l))