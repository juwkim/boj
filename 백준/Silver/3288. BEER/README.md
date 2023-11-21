# [Silver V] BEER - 3288 

[문제 링크](https://www.acmicpc.net/problem/3288) 

### 성능 요약

메모리: 108080 KB, 시간: 120 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션

### 제출 일자

2023년 11월 21일 10:15:45

### 문제 설명

<p>Dave is preparing his birthday party. Among other things, he brought non-alcoholic beer in bottles and put them in his refrigerator. He arranged them the following way: He put as much bottles he could in one row at bottom of the refrigerator. Then he put one bottle less on the bottles from the first row, such that each new bottle lies firmly on two bottles from the first row (thus making the second row). He continued to put bottles that way until he put only one bottle to the last row (see the picture below). He arranged the bottles so that all stopples faced him.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/adcdfe57-f6c9-432c-b721-4f579b762ad3/-/preview/" style="width: 100px; height: 83px;"></p>

<p>There is an arrow drawn on each stopple. An arrow on a stopple can point to one of the following four directions: up, right, down and left.</p>

<p>Dave tried to turn the bottles so that all arrows on the stopples point upwards. He tried to turn bottles and realized that turning one bottle will also turn some of the neighbouring bottles.</p>

<p>Write a program that will for given arrangement of arrows on stopples generate a sequence of simple turns that will help Dave to make all arrows point upwards. One simple turn consist of turning a bottle 90 degrees clockwise. If there is a bottle up left or up right of turned bottle, it will be turned 90 degrees counterclockwise at the same time. Therefore, one simple turn will change directions of three bottles at most.</p>

<p>Your program should for given directions of arrows generate any sequence of simple turns which will make all arrows point upwards. A pair of numbers determines a position of a bottle: the first number denotes a row containing the bottle, and the second number denotes the position of the bottle in the row. Rows are numbered from the bottom to the top (the lowest row is numbered by 1), and bottles in a row are numbered from left to right (the leftmost bottle is numbered by 1).</p>

<p>Each simple turn is determined by a position of a bottle that Dave needs to turn. Total number of simple turns should not exceed 1000.</p>

### 입력 

 <p>The first line of input file contains an integer N, 1 ≤ N ≤ 10, the number of bottles in the lowest row.</p>

<p>Each of the following N lines contains a sequence of letters denoting directions of arrows on stopples in the corresponding row. Letter U stands for up, L for left, D for down and R for right.</p>

### 출력 

 <p>The output file should contain a sequence of simple moves that solve the problem, one per line.</p>

<p>Two numbers, representing one simple move (a position of a bottle Dave needs to turn), should be written separated by a space character. The first number denotes a row containing the bottle and the second number stands for a position of that bottle.</p>

<p>Note: a solution needs not to be unique.</p>

