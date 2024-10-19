# [Silver II] Hoof, Paper, Scissors (Silver) - 14453 

[문제 링크](https://www.acmicpc.net/problem/14453) 

### 성능 요약

메모리: 124720 KB, 시간: 156 ms

### 분류

다이나믹 프로그래밍, 누적 합

### 제출 일자

2024년 10월 20일 02:22:55

### 문제 설명

<p>You have probably heard of the game "Rock, Paper, Scissors". The cows like to play a similar game they call "Hoof, Paper, Scissors".</p>

<p>The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each-other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. Hoof beats scissors (since a hoof can smash a pair of scissors), scissors beats paper (since scissors can cut paper), and paper beats hoof (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.</p>

<p>Farmer John wants to play against his prize cow, Bessie, at N games of "Hoof, Paper, Scissors" (1 ≤ N ≤ 100,000). Bessie, being an expert at the game, can predict each of FJ's gestures before he makes it. Unfortunately, Bessie, being a cow, is also very lazy. As a result, she tends to play the same gesture multiple times in a row. In fact, she is only willing to switch gestures at most once over the entire set of games. For example, she might play "hoof" for the first x games, then switch to "paper" for the remaining N−x games.</p>

<p>Given the sequence of gestures FJ will be playing, please determine the maximum number of games that Bessie can win.</p>

### 입력 

 <p>The first line of the input file contains N.</p>

<p>The remaining N lines contains FJ's gestures, each either H, P, or S.</p>

<p> </p>

### 출력 

 <p>Print the maximum number of games Bessie can win, given that she can only change gestures at most once.</p>

