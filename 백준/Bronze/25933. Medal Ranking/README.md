# [Bronze III] Medal Ranking - 25933 

[문제 링크](https://www.acmicpc.net/problem/25933) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>When different countries compete against each other (e.g., in the Olympics), they receive gold/silver/bronze medals. The countries can then be ranked in one of two ways: by “count” which is based on the total number of medals (regardless of the medal colors) or by “color” which is based on the number of gold medals (and silver medals if tied in gold medals, and bronze medals if tied in gold and silver).</p>

<p>Given the gold/silver/bronze medal counts for USA and Russia, you are to determine if USA wins in these two ranking methods.</p>

### 입력 

 <p>The first input line contains a positive integer, n, indicating the number of data sets to check. The sets are on the following n input lines, one set per line. Each set consists of 6 integers (each integer between 0 and 500 inclusive); the first three integers represent (respectively) the gold, silver, and bronze medal counts for USA; the last three integers provide this info for Russia (in same order).</p>

### 출력 

 <p>Print each input set. Then, on the next output line, print one of four messages (count, color, both, none), indicating how USA can win. USA will win by count if its total medal count is higher than the total for Russia. USA will win by color if it has more gold medals than Russia (if tied in gold, then USA must have more silver; if tied in gold and silver, then USA must have more bronze). Leave a blank line after the output for each test case.</p>

