# [Silver IV] Absolutely Acidic - 6770 

[문제 링크](https://www.acmicpc.net/problem/6770) 

### 성능 요약

메모리: 121876 KB, 시간: 1308 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>You are gathering readings of acidity level in a very long river in order to determine the health of the river. You have placed N sensors (2 ≤ N ≤ 2 000 000) in the river, and each sensor gives an integer reading R (1 ≤ R ≤ 1 000). For the purposes of your research, you would like to know the frequency of each reading, and find the absolute difference between the two most frequent readings.</p>

<p>If there are more than two readings that have the highest frequency, the difference computed should be the largest such absolute difference between two readings with this frequency. If there is only one reading with the largest frequency, but more than one reading with the second largest frequency, the difference computed should be the largest absolute difference between the most frequently occurring reading and any of the readings which occur with second-highest frequency</p>

### 입력 

 <p>The first line of input will be the integer N (2 ≤ N ≤ 2 000 000), the number of sensors. The next N lines each contain the reading for that sensor, which is an integer R (1 ≤ R ≤ 1 000). You should assume that there are at least two different readings in the input.</p>

### 출력 

 <p>Output the positive integer value representing the absolute difference between the two most frequently occurring readings, subject to the tie-breaking rules outlined above.</p>

