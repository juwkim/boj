A, B = map(int, input().split())
nums = [*range(1, 11)] * 2
nums.remove(A)
nums.remove(B)
ans = 0
equal_AB, mod = A == B, (A + B) % 10
for i in range(17):
    for j in range(i + 1, 18):
        a, b = nums[i], nums[j]
        if a == b:
            ans += (equal_AB and A > a)
        else:
            ans += (equal_AB or mod > (a + b) % 10)
print("%.3f" % (ans / 153))