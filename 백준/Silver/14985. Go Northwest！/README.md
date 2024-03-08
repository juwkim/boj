# [Silver III] Go Northwest! - 14985 

[문제 링크](https://www.acmicpc.net/problem/14985) 

### 성능 요약

메모리: 217532 KB, 시간: 952 ms

### 분류

조합론, 자료 구조, 해시를 사용한 집합과 맵, 수학, 정렬

### 제출 일자

2024년 3월 9일 06:38:15

### 문제 설명

<p>Go Northwest! is a game usually played in the park main hall when occasional rainy weather discourages the visitors from enjoying outdoor attractions.</p>

<p>The game is played by a pair of players and it is based entirely on luck, the players can hardly influence its outcome.</p>

<p>The game plan consists of one large map on the wall with N distinct towns displayed on it. Before the start of the game, the leader of the game hands a bowl filled with N identical balls to each player. Inside each ball, there is a reference to some town on the map. Each bowl contains references to all towns on the map.</p>

<p>When the game starts, one of the players randomly draws one ball from his/her bowl, opens it and reveals the town inside. Next, the other player randomly draws one ball form his/her bowl, opens it and also reveals the town inside.</p>

<p>If both towns are the same, the game ends in a draw. If the towns are not the same, the leader of the game highlights the towns on the map. If one of the towns lies exactly Northwest to the other, the first player wins the game. If one of the towns lies exactly Northeast to the other, the second player wins the game. In all other cases, the game ends in a draw. Two towns are considered to lie exactly Northwest or Northeast from each other, if the angle between the line connecting the towns and the horizontal axis is exactly 45 degrees.</p>

<p>It is clear that the chance of winning the game depends substantially on the layout of the towns on the map. All town coordinates are known in advance. You are asked to find the probability that there is a winner in the game.</p>

<p> </p>

### 입력 

 <p>There are more test cases. Each case starts with a line containing one integer N (1 ≤ N ≤ 10<sup>5</sup>) specifying the number of towns on the map. Next, there are N lines each of which contains two integers x and y separated by space and specifying the coordinates of one town on the map. The coordinates are standard Cartesian coordinates in the plane. The absolute value of any coordinate does not exceed 10<sup>9</sup>.</p>

### 출력 

 <p>For each test case, print a single line with one floating point number P denoting the probability that there is a winner in the game. P should be printed with the maximum allowed error of 10<sup>−6</sup>.</p>

