# [Silver V] 6789 - 17508 

[문제 링크](https://www.acmicpc.net/problem/17508) 

### 성능 요약

메모리: 30840 KB, 시간: 144 ms

### 분류

많은 조건 분기(case_work), 구현(implementation)

### 문제 설명

<p>Jaehyun likes digits. Among the 10 digits, 6, 7, 8, and 9 are his favorite. Therefore, he made a special card set consisting of only 6, 7, 8 and 9. </p>

<p>Currently, Jaehyun has $N\times M$ cards. Jaehyun wants to make a magical $N$ by $M$ matrix of cards. Each row of the matrix should contain $M$ cards. He already arranged his cards in a shape of $N$ by $M$ matrix.</p>

<p style="text-align: center;"><img alt="" src=""><br>
 </p>

<p style="text-align: center;"><em>Figure 1. Initial state, not point symmetric.</em></p>

<p>To be a magic matrix, the matrix must be point symmetrical: Rotating the matrix 180 degrees results in the same original matrix. For example, 8 is point symmetrical with itself, and 6 and 9 are point symmetrical with each other.</p>

<p>Jaehyun doesn't want to switch the position of the cards, so his goal is to make the matrix point symmetrical by only rotating the cards in their original positions.</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;"><em>Figure 2. After rotating two cards, they are point symmetric.</em></p>

<p>Find the minimum number of cards you have to turn to make a magic matrix.</p>

### 입력 

 <p>The first line contains two integers, $N$ and $M$. ($1 \le N,\ M \le 500$)</p>

<p>Each of the next $N$ lines contains a string of $M$ characters which denotes the numbers written in each card. It is guaranteed that each character is one of 6, 7, 8 or 9.</p>

### 출력 

 <p>Print the minimum number of cards you have to turn to make a magic matrix in the first line. If it is not possible to make a magic matrix, print "-1". (without quotes)</p>

