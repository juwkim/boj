# [Silver IV] Klingon Levels - 5716 

[문제 링크](https://www.acmicpc.net/problem/5716) 

### 성능 요약

메모리: 213988 KB, 시간: 1356 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>In a Latin American high school, the klingon language has become so popular that many of the students have begun learning this artificial language on their own. After becoming aware of the situation, the directors have decided to implement formal klingon courses. The problem is that kids have different starting levels of knowledge of the language. Therefore, the directors decided to offer two course levels: basic and advanced.</p>

<p>The school has several divisions, with each student belonging to exactly one division. Because of bureaucracy and schedule conflicts, students of different divisions cannot be in the sameklingon course. Also, to be fair, the basic and advanced klingon levels should be offered to all divisions, and have the same level of difficulty among the divisions.</p>

<p>Therefore, each division will be partitioned into two groups: one group will be assigned a basic level course, and the other group an advanced level course. It is possible, also, that a division does not contain any students in one of the levels.</p>

<p>To assign the levels, a klingon test has been previously taken by all students of the school, each getting an integer grade between 0 and 1000, inclusive. To accomplish the aforementioned goals, the school directors have decided that all students with a score greater than or equal to some T will be assigned the advanced level, and all students with a score less than T will be assigned the basic level.</p>

<p>However, they cannot decide on the best value of T. They would like a value that evenly splits all divisions. For this, they came up with a metric: They want the value of T that minimizes the accumulated difference, that is, the sum of the difference between the number of students in the two groups (basic and advanced) within each division.</p>

<p>For example, if the school has two divisions, where one division has 10 students in the basic level and 20 in the advanced level, while the other one has 17 and 15, respectively, the accumulated difference would be |10 − 20| + |17 − 15| = 12.</p>

### 입력 

 <p>There are several test cases. Each test case is given in several lines. The first line of each test case contains a single integer N (1 ≤ N ≤ 10<sup>4</sup>), the number of divisions in the school. 2 × N lines follow, with each division being described in two consecutive lines. The first line of each group of two contains a single integer K<sub>i</sub> (1 ≤ K<sub>i</sub> ≤ 10<sup>4</sup>) the number of students in division i. The second line contains K<sub>i</sub> integers between 0 and 1000, inclusive, separated by single spaces, representing the scores of each of the students in division i. You may assume that the total number of students within each test case (that is, the sum of the values of all K<sub>i</sub>) is not greater than 10<sup>5</sup>.</p>

<p>The last test case is followed by a line containing a single zero.</p>

### 출력 

 <p>For each test case, output a single line with a single integer representing the minimum value for the accumulated difference if T is chosen optimally.</p>

