n = int(input())
while True:
    if n % sum(map(int, [i for i in str(n)])) == 0:
        print(n)
        break
    n += 1