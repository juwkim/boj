from fractions import Fraction
ans = set()
for i in range(1, 1 + int(input())):
    for j in range(1, i):
        ans.add(Fraction(j, i))
print(len(ans) + 2)
print('0/1')
for num in sorted(ans):
    print(num)
print('1/1')