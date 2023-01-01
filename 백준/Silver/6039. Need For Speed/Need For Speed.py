def g(): return [*map(int, input().split())]

F, M, N = g()
nums = [g() for _ in range(N)]

max_force, max_mass, ans = F, M, 0
def solve(force, mass, mask, idx):
    global ans, max_force, max_mass
    if idx == N:
        if max_force * mass < force * max_mass:
            ans = mask
            max_force = force
            max_mass = mass
        elif max_force * mass == force * max_mass and mass < max_mass:
            ans = mask
            max_force = force
            max_mass = mass
        return
    solve(force, mass, mask, idx + 1)
    solve(force + nums[idx][0], mass + nums[idx][1], mask | (1 << idx), idx + 1)

solve(F, M, 0, 0)
if ans:
    idx = 1
    while ans:
        ans, r = divmod(ans, 2)
        if r:
            print(idx)
        idx += 1
else:
    print('NONE')