def solve(N, S):

    nearest_trash_bin_left = [-float('inf')] * N
    nearest_trash_bin_right = [float('inf')] * N

    for i in range(N):
        if S[i] == "1":
            nearest_trash_bin_left[i] = i
        elif i > 0:
            nearest_trash_bin_left[i] = nearest_trash_bin_left[i - 1]

    for i in range(N - 1, -1, -1):
        if S[i] == "1":
            nearest_trash_bin_right[i] = i
        elif i < N - 1:
            nearest_trash_bin_right[i] = nearest_trash_bin_right[i + 1]

    total_distance = 0
    for i in range(N):
        distance_to_left = i - nearest_trash_bin_left[i]
        distance_to_right = nearest_trash_bin_right[i] - i
        distance = min(distance_to_left, distance_to_right)

        total_distance += distance

    return total_distance


for t in range(1, 1 + int(input())):
    N = int(input())
    S = input()

    ans = solve(N, S)
    print(f'Case #{t}: {ans}')