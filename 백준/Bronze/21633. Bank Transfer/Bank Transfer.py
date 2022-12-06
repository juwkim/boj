from statistics import median
commission = 25 + 0.01 * int(input())
print(f"{median([commission, 100, 2000]):#.2f}")