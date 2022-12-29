probs = [*map(float, input().split())]
total = abs(3.5 - sum(label * prob for label, prob in enumerate(probs, 1)))
ans = total / max(probs)
print("%.3f" % ans)