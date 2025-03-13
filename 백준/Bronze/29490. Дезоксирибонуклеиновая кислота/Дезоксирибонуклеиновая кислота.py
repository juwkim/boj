s = input()
if input() in s + s[::-1].translate({65: 84, 84: 65, 71: 67, 67: 71}):
    print('Yes')
else:
    print('No')