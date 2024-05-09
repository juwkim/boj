s = input()
M = int("".join(sorted(s, reverse=True)))
m = int("".join(sorted(s)))
print(str(M - m).zfill(len(s)))