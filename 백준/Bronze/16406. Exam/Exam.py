k = int(input())
a, b = input(), input()
Len_a = len(a)
same = sum(i == j for i, j in zip(a, b))

print(Len_a - abs(k - same))