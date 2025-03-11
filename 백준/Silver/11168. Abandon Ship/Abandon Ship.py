def solve():
    orders = []
    invert_state = {}  # 상태 저장 (true: invert, false: re-invert)
    power_levels = {system: 100 for system in category3}  # 초기 전력 상태
    extra_power = 20
    
    for system in damaged:
        if system in category1:
            orders.append(f"recalibrate {system}")
        elif system in category2:
            if system not in invert_state:
                invert_state[system] = True
            if invert_state[system]:
                orders.append(f"invert {system}")
            else:
                orders.append(f"re-invert {system}")
            invert_state[system] = not invert_state[system]
        elif system in category3:
            power_levels[system] -= 10
            if power_levels[system] <= 10:
                orders.append("ABANDON SHIP. REPEAT. ALL HANDS ABANDON SHIP.")
                break
            if extra_power > 0:
                needed_power = 100 - power_levels[system]
                used_power = min(needed_power, extra_power)
                power_levels[system] += used_power
                extra_power -= used_power
            orders.append(f"divert all power to {system}")
    return orders

for _ in range(int(input())):
    A, B, C, D = map(int, input().split())
    category1 = [input() for _ in range(A)]
    category2 = [input() for _ in range(B)]
    category3 = [input() for _ in range(C)]
    damaged = [input() for _ in range(D)]
    for l in solve():
        print(l)