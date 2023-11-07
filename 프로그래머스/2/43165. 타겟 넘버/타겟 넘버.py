def dfs(idx, cur, numbers, target):
    if idx == len(numbers):
        return cur == target
    ans = 0
    ans += dfs(idx + 1, cur + numbers[idx], numbers, target)
    ans += dfs(idx + 1, cur - numbers[idx], numbers, target)
    return ans

def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    return answer