money = (500, 100, 50, 10, 5, 1)
N = 1000 - int(input())
count, i = 0, 0
while N:
    count += N // money[i]
    N %= money[i]
    i += 1
print(count)