l, r = map(int, input().split())
print([['Odd ', 'Even '][l == r] + str(2 * max(l, r)), 'Not a moose'][l + r == 0])