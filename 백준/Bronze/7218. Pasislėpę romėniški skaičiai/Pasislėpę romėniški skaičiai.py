input()
S = input()
l = "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"
ans = [i + 1 for i in range(12) if l[i] in S]
print(*ans)