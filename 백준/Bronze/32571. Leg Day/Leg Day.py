ans = ["💪"] * 31
for i in range(int(input())):
    s = input()
    if "rest" in s:
        ans[i] = "😴"
    elif "leg" in s:
        ans[i] = "🦵"
for i in range(0, 31, 7):
    print(i // 7, "".join(ans[i:i+7]))