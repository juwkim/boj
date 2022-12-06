g = lambda: [*map(int, input().split())]

N = int(input())
pos = None
odd, even = False, False

for i in range(N):
    nums = g()
    for j in range(N):
        if nums[j] == 1:
            if (i + j) & 1:
                odd = True
            else:
                even = True
        elif nums[j] == 2:
            if (i + j) & 1:
                pos = 1
            else:
                pos = 0

if pos == 1 and even and not odd:
    ans = 'Lena'
elif pos == 0 and odd and not even:
    ans = 'Lena'
elif not even and not odd:
    ans = 'Lena'
else:
    ans = 'Kiriya'
print(ans)