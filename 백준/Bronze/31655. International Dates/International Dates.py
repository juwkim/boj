A, B, _ = map(int, input().split('/'))
EU = A <= 31 and B <= 12
US = B <= 31 and A <= 12
if EU and US:
    print("either")
elif EU:
    print("EU")
else:
    print("US")