N = int(input())
num_check = 1
fraction_sum = 2

while True:
    if N <= num_check:
        break
    num_check += fraction_sum
    fraction_sum += 1

numerator = num_check - N + 1
denominator = fraction_sum - numerator

print(numerator, denominator)