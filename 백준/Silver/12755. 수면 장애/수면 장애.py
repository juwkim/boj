N = int(input())
size = 1
amount = 9
while N > size * amount:
    N -= size * amount
    size += 1
    amount *= 10
r, q = divmod(N-1, size)
print(str(int('1' + '0' * (size - 1)) + r)[q])