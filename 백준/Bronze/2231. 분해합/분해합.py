N = int(input())
generator = 0
for num in range(1, N):
    digit_sum = num + sum(map(int, str(num)))
    if digit_sum == N:
        generator = num
        break
print(generator)