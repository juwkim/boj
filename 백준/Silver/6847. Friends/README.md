# [Silver II] Friends - 6847 

[문제 링크](https://www.acmicpc.net/problem/6847) 

### 성능 요약

메모리: 113620 KB, 시간: 124 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 1월 7일 20:40:08

### 문제 설명

<p>In a certain school, it has been decided that students are spending too much time studying and not enough time socializing. To address this situation, it has been decided to give every student a friend. Friendship is one-way. That is, if Janet is assigned to be Sarah’s friend, Janet must be friendly to Sarah, but Sarah is not required to reciprocate.</p>

<p>The assignment of friends is done by computer using student numbers. Every student is assigned exactly one friend. Sometimes, a ‘circle of friends’ occurs. For example, if Marc is assigned Fred, Fred is assigned Lori, Lori is assigned Jean, and Jean assigned Marc, we have a circle of 4 friends containing Marc, Fred, Lori, and Jean. In the circle, we can say that Marc has a separation of 0 from Fred, of 1 from Lori, of 2 from Jean, and of 3 from Marc.</p>

<p>Your task it to identify, given the computer assignment of friends, whether two students are in the same circle of friends, and if so, determine their separation.</p>

### 입력 

 <p>Input begins with a single integer n (2 ≤ n ≤ 9999), on a line by itself, indicating the number of students in the class. The next n lines contain the computer assignment of friendship. An assignment is of the form x y (where 1 ≤ x ≤ 9999, 1 ≤ y ≤ 9999, x 6= y). For example, 1234 8765 is a possible friendship assignment indicating that student 1234 must be friends with student 8765.</p>

<p>Following the friendship assignments, there are a series of lines containing two student numbers, separated by a single whitespace. These lines represent the pairs of students that you will determine if they are in same circle of friends and, if so, their separation. The last line of input can be identified by the use of the 0 0 as the friend assignment.</p>

### 출력 

 <p>For each case, you are to print, on a separate line, either Yes or No depending on whether they are in the same circle of friends. If the answer is Yes, follow the output Yes with a single whitespace and then an integer indicating the friend’s separation.</p>

