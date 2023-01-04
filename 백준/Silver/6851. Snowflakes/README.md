# [Silver IV] Snowflakes - 6851 

[문제 링크](https://www.acmicpc.net/problem/6851) 

### 성능 요약

메모리: 286724 KB, 시간: 1292 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 정렬(sorting)

### 문제 설명

<p>You may have heard that no two snowflakes are alike. Your task is to write a program to determine whether this is really true. Your program will read information about a collection of snowflakes, and search for a pair that may be identical.</p>

<p>Each snowflake has six arms. For each snowflake, your program will be provided with a measurement of the length of each of the six arms. Any pair of snowflakes which have the same lengths of corresponding arms should be flagged by your program as possibly identical.</p>

### 입력 

 <p>The first line of input will contain a single integer n, 0 < n ≤ 100000, the number of snowflakes to follow. This will be followed by n lines, each describing a snowflake. Each snowflake will be described by a line containing six integers (each integer is at least 0 and less than 10000000), the lengths of the arms of the snowflake. The lengths of the arms will be given in order around the snowflake (either clockwise or counterclockwise), but they may begin with any of the six arms. For example, the same snowflake could be described as 1 2 3 4 5 6 or 4 3 2 1 6 5.</p>

### 출력 

 <p>If all of the snowflakes are distinct, your program should print the message:</p>

<p><code>No two snowflakes are alike.</code></p>

<p>If there is a pair of possibly identical snowflakes, your program should print the message:</p>

<p><code>Twin snowflakes found.</code></p>

