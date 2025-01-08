ans = []
for c in input():
    t = c if c.isdigit() else '0'
    ans.append(f"({t})+")
ans.append("0")
print(*ans, sep="")