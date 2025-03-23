import sys
input = sys.stdin.readline

while (L:=float(input())) > 0:
    nums = []
    while True:
        x1, x2 = map(float, input().split())
        if x1 > x2:
            break
        if x2 <= 0 or x1 >= L:
            continue
        nums.append((max(0, x1), 1))
        nums.append((min(L, x2), 0))
    st = []
    for x, typ in sorted(nums):
        if typ:
            st.append(x)
        else:
            num = st.pop()
            if not st:
                L -= x - num
    print(f"The total planting length is {L:.1f}")