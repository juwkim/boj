W = float(input())
H = float(input())
BMI = W / (H * H)
if BMI > 25:
    ans = 'Overweight'
elif BMI < 18.5:
    ans = 'Underweight'
else:
    ans = 'Normal weight'
print(ans)