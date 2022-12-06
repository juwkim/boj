txt = input()
print(1 + sum(x >= y for x, y in zip(txt, txt[1:])))