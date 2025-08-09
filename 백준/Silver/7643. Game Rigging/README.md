# [Silver I] Game Rigging - 7643 

[문제 링크](https://www.acmicpc.net/problem/7643) 

### 성능 요약

메모리: 136500 KB, 시간: 264 ms

### 분류

그래프 이론, 그래프 탐색

### 제출 일자

2025년 8월 9일 22:14:40

### 문제 설명

<p>You’ve decided to host a StarCraft II tournament to decide who is the very best StarCraft II player at Stanford. A lot of your friends are entering, and you want one of them to win because the prize is two tickets to the next StarCraft II World Finals! Luckily, you get to arrange the games and you have some information about which players will beat which other ones, i.e. match-ups which have a guaranteed outcome. The tournament is played as a series of games where in each game two players (of your choice) who have not yet been eliminated play each other. This continues until only one player remains, and he is the winner. Can you set the tournament up so that one of your friends wins?</p>

### 입력 

 <p>The input consists of multiple test cases. Each test case will start with two integers N (2 ≤ N ≤ 100,000), the number of players in the tournament, K (1 ≤ K ≤ N), the number of your friends in the tournament, and M (0 ≤ M ≤ 100,000), the number of match-ups for which you know the outcome. The next line will contain K integers between 1 and N, indicating which of the players are your friends (indices corresponding to the order of the input). The following M lines will contain two integers each; a line containing A B indicates that if players A and B play each other, player A will always beat player B. Input is followed by a single line with N = K = 0, which should not be processed.</p>

### 출력 

 <p>For each test case, output one line which contains either “yes” or “no” (without quotes) indicating whether you can guarantee that one of your friends wins the tournament.</p>

