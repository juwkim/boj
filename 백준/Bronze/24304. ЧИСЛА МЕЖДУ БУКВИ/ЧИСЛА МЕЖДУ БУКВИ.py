n = int(input())
buf = []
for i in input():
    if i.isalpha():
        buf.append(' ')
    else:
        buf.append(i)
nums = [*map(int, ''.join(buf).split())]
if nums:
    for num in nums:
        print(n * num)
else:
    print('N/A')