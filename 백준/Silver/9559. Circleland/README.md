# [Silver II] Circleland - 9559 

[문제 링크](https://www.acmicpc.net/problem/9559) 

### 성능 요약

메모리: 154680 KB, 시간: 268 ms

### 분류

많은 조건 분기, 누적 합

### 제출 일자

2025년 1월 8일 04:08:20

### 문제 설명

<p>You are visiting circleland, and you have long waited to visit their famous art exhibition. The exhibition has N rooms arranged in a cycle. In every room, there are some artistic pieces. The rooms are named R<sub>1</sub>, R<sub>2</sub>, ..., R<sub>N</sub> . There are also N corridors, named C<sub>1</sub>, C<sub>2</sub>, ..., C<sub>N</sub> , of lengths L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>N</sub> , respectively. Each corridor Ci connects the two rooms R<sub>i</sub> and R<sub>i+1</sub>, except C<sub>N</sub> which connects R<sub>N</sub> and R<sub>1</sub>. Thus, the whole exhibition forms a cycle. You can walk in both directions in every corridor.</p>

<p>There is a single entrance to the exhibition in room R<sub>1</sub>, but there are exits in every room. As there is nothing interesting to see in the corridors, you would like to spend the least effort walking through corridors in the exhibition. Compute the minimum total distance you need to walk in corridors such that you enter from the entrance, exit from any exit and visit all rooms.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. The first line of the input will be a single integer T, the number of test cases (1 ≤ T ≤ 100). Next T lines contain the test cases, each on a single line.</p>

<p>Each case starts with an integer N, the number of rooms in the exhibition (2 ≤ N ≤ 100, 000), followed by N numbers, the lengths of the corridors, L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>N</sub> , in this order (1 ≤ L<sub>i</sub> ≤ 1, 000, 000).</p>

<p>The sum of the lengths of all corridors will not exceed 1, 000, 000, 000.</p>

### 출력 

 <p>For each test case, output, on a single line, a single number representing the minimum total distance you have to walk in corridors such that you visit all rooms.</p>

