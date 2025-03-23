def min_max_stamp_size(n, k, sections):
    left, right = 1, max(sections)  # 가능한 s의 범위: 1 ~ 최대 섹션 길이
    answer = right  # 최적의 s를 저장

    while left <= right:
        mid = (left + right) // 2  # 중간값 s 설정
        total_stamps = sum((p + mid - 1) // mid for p in sections)  # 올림 연산

        if total_stamps <= k:  # 필요한 도장 수가 k 이하면 가능한 s
            answer = mid
            right = mid - 1  # 더 작은 s 시도
        else:  # 필요한 도장 수가 k 초과면 s를 증가
            left = mid + 1  

    return answer  # 최소 가능한 s 반환

# 입력 받기
n, k = map(int, input().split())
sections = [int(input()) for _ in range(n)]

# 결과 출력
print(min_max_stamp_size(n, k, sections))