s = input()
print(sum(min(26-abs(ord(x)-ord(y)),abs(ord(x)-ord(y))) for x, y in zip('A'+ s, s)))