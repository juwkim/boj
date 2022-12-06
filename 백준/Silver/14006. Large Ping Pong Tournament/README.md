# [Silver IV] Large Ping Pong Tournament - 14006 

[문제 링크](https://www.acmicpc.net/problem/14006) 

### 성능 요약

메모리: 39224 KB, 시간: 148 ms

### 분류

애드 혹(ad_hoc), 정렬(sorting)

### 문제 설명

<p><strong>"Don't underestimate my strength."</strong> - Dudu, 2015</p>

<p><strong>Note:</strong> This problem is identical to Small Ping Pong Tournament, but with larger bounds.</p>

<p>Dudu is enjoying his time in Thailand and has decided to compete in a local ping pong tournament.</p>

<p>For this tournament a game of ping pong occurs between two players. It lasts for a fixed amount of time, after which the player with more points is declared to be the winner. In the case of a tie an arm wrestling match is used to determine who wins.</p>

<p>The tournament starts with a total of 2<sup>N</sup> players, including Dudu, and proceeds in rounds. In each round, all K remaining players are formed into pairs to play games of ping pong. The loser of each game is eliminated, while the K/2 winners continue on to the next round. The last player remaining is declared the winner.</p>

<p>After the tournament, the organizers realized that the only information they recorded from the tournament is the total number of points each player scored. They didn't record who played with whom, and who won each game. In particular, they forgot to record who the winner was!</p>

<p>You are given the total points scored by each player across all of his games. You also know that Dudu is very strong, and never loses at arm wrestling. Determine whether it is possible for Dudu to have been the champion.</p>

### 입력 

 <p>The input will start with a line containing a single integer N. The following 2<sup>N</sup> lines will each contain an integer indicating the total number of points scored by some player. Dudu's score is given first.</p>

<p>0 ≤ N ≤ 18. All scores will be non-negative integers ≤ 10<sup>9</sup>.</p>

### 출력 

 <p>Output "YES" if it possible for Dudu to have won the tournment, and output "NO" otherwise.</p>

