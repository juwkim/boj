def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

l = open(0).read().split()

if len(l) != 3:
    print(0)
elif not all(num[0] != '0' and num.isdecimal() for num in l):
    print(0)
else:
    a, b, c = map(int, l)
    if 3 < a <= pow(10, 9) and a % 2 == 0 and isPrime(b) and isPrime(c) and a == b + c:
        print(1)
    else:
        print(0)