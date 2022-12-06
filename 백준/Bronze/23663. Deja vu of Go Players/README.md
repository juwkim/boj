# [Bronze III] Deja vu of Go Players - 23663 

[문제 링크](https://www.acmicpc.net/problem/23663) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

게임 이론(game_theory), 그리디 알고리즘(greedy), 구현(implementation)

### 문제 설명

<p>An ordinary sequence rather than magic codes? Rikka's opinion is much more important than the "truth" itself. She soon felt sleepy and fell asleep to take a trip to dreamlands in passing.</p>

<p>Rikka found two elders playing Go game when her sanity got back. The ethereal clouds, hardy vigorous pines, and rugged rocks shocked her. A fiction <em>isekai</em>! Excited Rikka's eyes ran around and around and focused on the Go chessboard in the end.</p>

<p>She found that the two players, wearing white and red respectively, were not playing Go game --- they divided the black and white chess pieces into some piles, and were taking turns removing them. They kept silent for her questions, so Rikka had to stand there and keep her eyes on the chessboard.</p>

<p>They seemed to be playing an unexpectedly simple game. The red player has $n$ black piles and its opponent has $m$ white piles at the beginning. They take turns removing any positive number of chess pieces from arbitrary one of their assigned piles. Red goes first, and the player who first removes all chess pieces assigned to oneself "wins", and the other player has to drink.</p>

<p>Drinking is illegal for minors in Japan, so Rikka wonders if she can ensure to win when she is the red player.</p>

### 입력 

 <p>The first line contains an integer $T (1\le T \le 100) $, the number of test cases. Then $T$ test cases follow.</p>

<p>The input format of each test case is as follows:</p>

<p>The first line contains two integers $n,m (1\le n,m \le 100)$, the numbers of piles of the red and the white player, respectively.</p>

<p>The following line contains $n$ integers $a_i (1 \leq a_i \leq 10^9)$, in which each integer indicates the number of pieces in a black pile of the red player.</p>

<p>The following line contains $m$ integers $b_i (1 \leq b_i \leq 10^9)$, in which each integer indicates the number of pieces in a white pile of the white player.</p>

### 출력 

 <p>Output a string in the only line, "<code>Yes</code>" if the red player who moves first can ensure to win, or "<code>No</code>" otherwise, without quotation marks.</p>

