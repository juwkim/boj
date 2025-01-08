# [Silver II] BUHA - 3262 

[문제 링크](https://www.acmicpc.net/problem/3262) 

### 성능 요약

메모리: 111040 KB, 시간: 128 ms

### 분류

구현

### 제출 일자

2025년 1월 9일 04:45:15

### 문제 설명

<p>Boško and Suško are playing an interesting game on a board made of rectangular fields arranged in A rows and B columns.</p>

<p>When the game starts, Suško puts its virtual pillbox on one field the board. Then Boško selects fields on which he will throw his virtual bombs and Suško replies for each bomb if his bunker is in a range.</p>

<p>Range of bomb with diameter P that is thrown on field (R,S) is a rectangle with sides parallel to sides of the board, with field (R,S) in its center and length of each side is P.</p>

<p>Write a program that will help Boško to find out on how many fields could have been placed Suško’s pillbox after some bombs have been thrown.</p>

### 입력 

 <p>First line of input file contains three integers: A, B and K, 1 ≤ A,B,K ≤ 100. A represents number of rows, B number of columns and K number of thrown bombs.</p>

<p>Each of the next K lines contains integers R, S, P and T, describing a bomb thrown at the field in Rth row and Sth column with diameter P, 1 ≤ P ≤ 99, P is odd. T equals 1 if the pillbox is in a range if that bomb, otherwise it is 0.</p>

### 출력 

 <p>Write to the output file the number of fields on which could have been placed bunker. </p>

