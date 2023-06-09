a, b = int(input()), int(input())
ans = 0
for i in range(1, 10):
    j = 10 - i
    ans += a >= i and b >= j

if ans == 1:
    print("There is 1 way to get the sum 10.")
else:
    print(f'There are {ans} ways to get the sum 10.')