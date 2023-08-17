for i in range(3):
    s = input()
    if s.isnumeric():
        num = int(s) + (3 - i)
if num % 3 == 0 and num % 5 == 0:
    ans = "FizzBuzz"
elif num % 3 == 0:
    ans = "Fizz"
elif num % 5 == 0:
    ans = "Buzz"
else:
    ans = num
print(ans)