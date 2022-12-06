import sys
gimbap = [list(map(int, line.split())) for line in sys.stdin]
del gimbap[1]
price = min([store[0] * 1000 / store[1] for store in gimbap])
print(price)