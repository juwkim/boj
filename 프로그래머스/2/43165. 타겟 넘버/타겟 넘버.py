from itertools import product

def solution(numbers, target):
    answer = list(map(sum, product(*[(x, -x) for x in numbers]))).count(target)
    return answer