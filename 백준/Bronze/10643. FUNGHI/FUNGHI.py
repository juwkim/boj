s = [int(i) for i in open(0)]
a = list(sum(s[i:i+4])for i in range(4))
print(max(max(a), sum(s) - min(a)))