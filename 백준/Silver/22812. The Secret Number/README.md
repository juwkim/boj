# [Silver I] The Secret Number - 22812 

[문제 링크](https://www.acmicpc.net/problem/22812) 

### 성능 요약

메모리: 111464 KB, 시간: 132 ms

### 분류

임의 정밀도 / 큰 수 연산, 다이나믹 프로그래밍

### 제출 일자

2025년 8월 10일 15:35:33

### 문제 설명

<p>Your job is to find out the secret number hidden in a matrix, each of whose element is a digit ('0'-'9') or a letter ('A'-'Z'). You can see an example matrix in Figure 1.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/22f6177a-c9d6-4bdd-aa93-92b249baf90b/-/preview/"></p>

<p style="text-align: center;">Figure 1: A Matrix</p>

<p>The secret number and other non-secret ones are coded in a matrix as sequences of digits in a decimal format. You should only consider sequences of digits <i>D</i><sub>1</sub> <i>D</i><sub>2</sub> ... <i>D</i><sub><i>n</i></sub> such that <i>D</i><sub><i>k</i>+1</sub> (1 <= <i>k</i> < <i>n</i>) is either right next to or immediately below <i>D</i><sub><i>k</i></sub> in the matrix. The secret you are seeking is the largest number coded in this manner.</p>

<p>Four coded numbers in the matrix in Figure 1, i.e., 908820, 23140037, 23900037, and 9930, are depicted in Figure 2. As you may see, in general, two or more coded numbers may share a common subsequence. In this case, the secret number is 23900037, which is the largest among the set of all coded numbers in the matrix.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/707be2a1-e57e-4fcf-98ee-f6464f44ac5b/-/preview/"></p>

<p style="text-align: center;">Figure 2: Coded Numbers</p>

<p>In contrast, the sequences illustrated in Figure 3 should be excluded: 908A2 includes a letter; the fifth digit of 23149930 is above the fourth; the third digit of 90037 is below right of the second.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9fd5b7fe-dc13-43b4-9d5f-49b4ed6eae8d/-/preview/"></p>

<p style="text-align: center;">Figure 3: Inappropriate Sequences</p>

<p>Write a program to figure out the secret number from a given matrix.</p>

### 입력 

 <p>The input consists of multiple data sets, each data set representing a matrix. The format of each data set is as follows.</p>

<pre><i>W</i> <i>H</i>
<i>C</i><sub>11</sub><i>C</i><sub>12</sub> ... <i>C</i><sub>1<i>W</i></sub>
<i>C</i><sub>21</sub><i>C</i><sub>22</sub> ... <i>C</i><sub>2<i>W</i></sub>
...
<i>C</i><sub><i>H</i>1</sub><i>C</i><sub><i>H</i>2</sub> ... <i>C</i><sub><i>HW</i></sub>
</pre>

<p>In the first line of a data set, two positive integers <i>W</i> and <i>H</i> are given. <i>W</i> indicates the width (the number of columns) of the matrix, and <i>H</i> indicates the height (the number of rows) of the matrix. <i>W+H</i> is less than or equal to 70.</p>

<p><i>H</i> lines follow the first line, each of which corresponds to a row of the matrix in top to bottom order. The <i>i</i>-th row consists of <i>W</i> characters <i>C</i><sub><i>i</i>1</sub><i>C</i><sub><i>i</i>2</sub> ... <i>C</i><sub><i>iW</i></sub> in left to right order. You may assume that the matrix includes at least one non-zero digit.</p>

<p>Following the last data set, two zeros in a line indicate the end of the input.</p>

### 출력 

 <p>For each data set, print the secret number on a line. Leading zeros should be suppressed.</p>

