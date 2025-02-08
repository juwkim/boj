n, k = map(int, input().split())
a = {2 * n}
for i in range(k):
	newa = set()
	for apple in a:
		newa.add(apple - 1)
		if apple % 2 == 0:
			newa.add(apple >> 1)
	a = newa
a = sorted(num / 2 for num in a if num >= 0)
print(len(a))
print(*a)