import sys
input = sys.stdin.readline

def get_span_list(arr):
    span_list = [0] * (len(arr))
    winner_list = []
    for i in range(len(arr) - 1, -1, -1):
        while winner_list and arr[winner_list[-1]] <= arr[i]:
            winner_list.pop()
        if winner_list:
            h = winner_list[-1]
        else:
            h = len(arr)
        span_list[i] = h - i
        winner_list.append(i)
    return span_list

for step in range(1, 1 + int(input())):
    E, R, N = map(int, input().split())
    nums = [*map(int, input().split())]
    span_list = get_span_list(nums)
    ans, cur = 0, E
    for i in range(N):
        if i + span_list[i] == N:
            now = cur
        else:
            now = max(0, min(cur, (cur + span_list[i] * R) - E))
        cur = min(E, cur + R - now)
        ans += nums[i] * now
    print(f'Case #{step}: {ans}')