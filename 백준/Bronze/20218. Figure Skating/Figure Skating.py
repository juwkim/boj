n = int(input())
predicted = [input() for _ in range(n)]
final = [input() for _ in range(n)]
diff = [i - final.index(predicted[i]) for i in range(n)]
max_diff = max(diff)
print(predicted[diff.index(max_diff)] if max_diff else "suspicious")