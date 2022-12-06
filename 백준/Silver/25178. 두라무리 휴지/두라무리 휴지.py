N = int(input())
a = [*input()]
b = [*input()]
ans = 'YES'
vowel = set('aeiou')
if a[0] != b[0] or a[-1] != b[-1]:
    ans = 'NO'
elif sorted(a) != sorted(b):
    ans = 'NO'
else:
    tmp1 = [i for i in a if i not in vowel]
    tmp2 = [i for i in b if i not in vowel]
    if tmp1 != tmp2:
        ans = 'NO'
print(ans)