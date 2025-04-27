# [Silver II] Best Buddies - 11313 

[문제 링크](https://www.acmicpc.net/problem/11313) 

### 성능 요약

메모리: 165152 KB, 시간: 540 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 정렬, 트리를 사용한 집합과 맵

### 제출 일자

2025년 4월 27일 19:20:29

### 문제 설명

<p>You have signed up for the annual Calgary Collegiate Programming Contest. Unlike previous years, participants are not choosing their own team members, but are assigned to teams as follows. Consider we list all participants in alphabetic order. Then Team 1 consists of the first three participants in this order. Team 2 consists of the next three participants in this order. Assume that the number N of participants is divisible by 3 so that every team has exactly 3 team members.</p>

<p>Assume that every participant has exactly one first name and exactly one last name, the name is spelled over the alphabet {a, . . . , z}, and that no two participants carry the exact same name. The alphabetic order we choose, is to first sort in lexicographically ascending order with respect to last names, and then, when necessary, with respect to first names. So john smith is alphabetized after carla smith, but before bob taylor.</p>

<p>Given the name of a participant, output the names of the participant’s two team mates.</p>

### 입력 

 <p>The first line of the input contains an integer, N, the number of participants (3 ≤ N ≤ 99, 999). Then follows N lines, each containing the first name and last name of the participant. Both first and last name consist of at least 2 and at most 16 lower case characters of English alphabet. The next line contains an integer, Q, the number of queries (1 ≤ Q ≤ N). Then follows Q lines, each containing the first name and last name of the participant. The queried names are guaranteed to exist in the original list.</p>

### 출력 

 <p>For each of the Q test cases, output the names of the two team mates in the described order.</p>

