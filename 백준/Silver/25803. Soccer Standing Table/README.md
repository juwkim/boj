# [Silver III] Soccer Standing Table - 25803 

[문제 링크](https://www.acmicpc.net/problem/25803) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘, 조합론, 수학

### 제출 일자

2024년 5월 2일 02:41:45

### 문제 설명

<p>In soccer, a win is worth 3 points, draw (tie) is worth 1 point, and loss is worth zero points. Soccer standing tables show the following info for each team: number of matches played (MP), number of wins (W), number of draws (D), number of losses (L), and total number of points (Pts). For example, the entry:</p>

<pre>USA 11 5 4 2 19</pre>

<p>Indicates USA has played 11 matches, won 5 of them, drew 4 matches and lost 2, for a total number of points of 19 (5*3 + 4*1).</p>

<p>Even though the info is complete and helpful, some publications/websites list the numbers in different orders, e.g., the number of losses may be listed before the number of draws. And, if the columns are not labeled as to what they represent, that causes confusion.</p>

<p>Given five integers representing the entry for a soccer team, print these numbers in the order of MP-W-D-L-Pts.</p>

### 입력 

 <p>There is only one input line: it contains five integers, each between 0 and 300, inclusive. Assume that the input represents a valid entry, e.g., MP = W + D + L. Also assume that the input will not be all zeros, i.e., some games have been played.</p>

### 출력 

 <p>Print the numbers in the order of MP-W-D-L-Pts. Assume that there will be exactly one valid answer.</p>

