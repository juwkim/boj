# [Silver IV] War on Weather - 4282 

[문제 링크](https://www.acmicpc.net/problem/4282) 

### 성능 요약

메모리: 117144 KB, 시간: 268 ms

### 분류

구현(implementation)

### 문제 설명

<p>After an unprovoked hurricane attack on the south shore, Glorious Warrior has declared war on weather. The first salvo in this campaign will be a coordinated pre-emptive attack on as many tropical depressions as possible. GW reckons that the attack will neutralize the tropical depressions before they become storms, and dissuade others from forming.<br>
GW has at his disposal k space-to-earth killer satellites at various locations in space. m tropical depressions are known to exist at various locations on the earth's surface. Each satellite can attack any number of targets on the earth provided there is line of sight between the satellite and each target. How many different targets can be hit?</p>

### 입력 

 <p>The input consists of several test cases. Each case begins with a line containing integers 0 < k, m ≤ 100 as defined above. k lines follow, each giving x,y,z - the location in space of a satellite at the scheduled time of attack. m lines then follow, each giving x,y,z - the location of a target tropical depression. Assume the earth is a sphere centred at (0,0,0) with circumference 40,000 km. All targets will be on the surface of the earth (within 10<sup>-9</sup> km) and all satellites will be at least 50 km above the surface. A line containing 0 0 follows the last test case.</p>

### 출력 

 <p>For each test case, output a line giving the total number of targets that can be hit. If a particular target falls within 10<sup>-8</sup> km of the boundary between being within line-of-sight and not, it may be counted either way. (That is, you need not consider rounding error so long as it does not exceed 10<sup>-8</sup> km.)</p>

