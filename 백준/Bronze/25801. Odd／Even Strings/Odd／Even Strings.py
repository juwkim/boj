from collections import Counter
a = [i&1 for i in Counter(input()).values()]
if all(a):
    print(1)
elif all(i == 0 for i in a):
    print(0)
else:
    print("0/1")