s=input()
print(*sorted(set(s),key=s.index),sep='')