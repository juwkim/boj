a = int(input()) % 8
ans = min(a, 10 - a)
print([ans, 2][ans == 0])