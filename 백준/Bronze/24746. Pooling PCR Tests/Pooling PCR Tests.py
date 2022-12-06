p = 1 - float(input())
print(min(range(2, 17), key=lambda N: 1 - p**N + p**N / N))