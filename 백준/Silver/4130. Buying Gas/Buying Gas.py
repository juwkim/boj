# import sys
# g = lambda: [*map(int, sys.stdin.readline().split())]

# n, m, d = g()
# nums = [g() for _ in range(m)]

def min_gas_stops(capacity, stations, distance):
    stations.append((distance, 0))  # 도착 지점을 하나의 주유소로 간주
    stations.sort()
    
    max_range = capacity * 10  # 한 번 가득 채웠을 때 이동 가능한 최대 거리
    stops = 0
    curr_pos = 0
    tank = max_range
    idx = 0
    
    while curr_pos < distance:
        if tank >= distance - curr_pos:
            return stops  # 현재 연료로 도착 가능하면 종료
        
        max_reach = -1
        best_idx = -1
        
        while idx < len(stations) and stations[idx][0] <= curr_pos + tank:
            if max_reach < stations[idx][0]:
                max_reach = stations[idx][0]
                best_idx = idx
            idx += 1
        
        if best_idx == -1:
            return -1  # 도달할 수 있는 주유소가 없음
        
        curr_pos = stations[best_idx][0]
        tank = max_range  # 연료를 가득 채움
        stops += 1
    
    return stops

# 입력 받기
n, m, d = map(int, input().split())
stations = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(min_gas_stops(n, stations, d))
