s=input()
print(*sorted({*s},key=s.find),sep='')