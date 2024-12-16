c, d = map(int, input().split())
aprv, bprv = 0, 0
a, b = 10**6, 10**6
for i, s in enumerate(input().split(), c):
    match s:
        case "Fizz":
            a = min(a, i - aprv)
            aprv = i
        case "Buzz":
            b = min(b, i - bprv)
            bprv = i
        case "FizzBuzz":
            a = min(a, i - aprv)
            b = min(b, i - bprv)
            aprv = bprv = i
print(a, b)