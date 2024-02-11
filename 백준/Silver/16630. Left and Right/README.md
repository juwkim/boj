# [Silver III] Left and Right - 16630 

[문제 링크](https://www.acmicpc.net/problem/16630) 

### 성능 요약

메모리: 40388 KB, 시간: 252 ms

### 분류

그리디 알고리즘

### 제출 일자

2024년 2월 12일 02:00:35

### 문제 설명

<p>With modern technology advancement, it is now possible to deliver mail with a robot! There is a neighborhood on a long horizontal road, on which there are n houses numbered 1 to n from left to right. Every day a mail delivery robot receives a pile of letters with exactly one letter for each house. Due to mechanical restrictions, the robot cannot sort the letters. It always checks the letter on top of the pile, visits the house that should receive that letter and delivers it. The robot repeats this procedure until all the letters are delivered. As a result, each of the n houses is visited by the robot exactly once during the mail delivery of a single day.</p>

<p>The mail delivery robot has a tracking device that records its delivery route. One day the device was broken, and the exact route was lost. However, the technical team managed to recover the moving directions of the robot from the broken device, which are represented as a string consisting of n − 1 letters. The i-th letter of the string is ‘L’ (or ‘R’) if the (i + 1)-th house visited by the robot is on the left (or right) of the i-th house visited. For example, if n = 4 and the robot visited the houses in the order of 2, 4, 3, 1, its moving directions would be “RLL”.</p>

<p>With the moving directions, it may be possible to determine the order in which the robot visited the houses. The technical team has asked you to write a program to do that. There can be multiple orders producing the same moving directions, among which you should find the lexicographically earliest order.</p>

### 입력 

 <p>The input has a single integer n (2 ≤ n ≤ 2 · 10<sup>5</sup>) on the first line. The second line has a string of length n − 1 consisting of letters ‘L’ and ‘R’ giving the moving directions of the robot.</p>

### 출력 

 <p>Output the lexicographically earliest order in which the robot may have visited the houses and delivered the letters according to the moving directions.</p>

