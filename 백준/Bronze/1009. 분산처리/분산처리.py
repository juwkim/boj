# a의 b 제곱 mod 10 연산
def A_to_the_Bth_power(a, b):
    if a == 1 or a == -1 or b == 0:
        return 1
    if a >= 6:
        a %= -10
    if b % 2:
        return a * A_to_the_Bth_power(a**2, b // 2)
    else:
        return A_to_the_Bth_power(a**2, b // 2)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    num = A_to_the_Bth_power(a, b) % 10
    if num == 0:
        num = 10
    print(num)