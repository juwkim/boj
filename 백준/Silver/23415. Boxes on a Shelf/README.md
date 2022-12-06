# [Silver IV] Boxes on a Shelf - 23415 

[문제 링크](https://www.acmicpc.net/problem/23415) 

### 성능 요약

메모리: 34692 KB, 시간: 280 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 물리학(physics), 정렬(sorting)

### 문제 설명

<p>Varya has a barn where she stores $n$ boxes with important stuff. She recently nailed another shelf to the barn wall. Now she wants to put as many boxes as possible on the new shelf.</p>

<p>We shall look at the wall with the shelf as a plane. The shelf is then a horizontal segment of length $L$. There is empty space to the left and to the right of the shelf, which we can consider to be infinite. Box number $i$ is a rectangle with sides $a_i$ and $b_i$.</p>

<p>A box can stand on the shelf and not fall when one of its sides, or a part of it, lies on the shelf, and the center of the box is above an interior point of the shelf. Boxes can be placed only on the shelf, close to the wall: they can not be placed on top of other boxes or in several layers.</p>

<p>Find is the maximum number of boxes Varya can put on the shelf.</p>

### 입력 

 <p>The first line contains an integer $n$: the number of boxes ($1 \le n \le 100\,000$). Each of the following $n$ lines contains two integers $a_i$ and $b_i$: the sides of the respective box ($1 \le a_i, b_i \le 100\,000$). The last line contains an integer $L$: the length of the shelf ($1 \le L \le 10^9$).</p>

### 출력 

 <p>Print one integer: the maximum number of boxes Varya can put on the shelf so that they don't fall off.</p>

