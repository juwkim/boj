# [Silver I] Fantasy Draft - 17875 

[문제 링크](https://www.acmicpc.net/problem/17875) 

### 성능 요약

메모리: 119112 KB, 시간: 164 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 큐, 시뮬레이션, 집합과 맵

### 제출 일자

2025년 5월 12일 03:13:55

### 문제 설명

<p>In fantasy hockey, there are n team owners that each selects k hockey players. To determine which owner gets which players, the owners hold a draft.</p>

<p>The draft proceeds as follows: the first owner may select any player, then the second owner can select any player except the player taken first and so on. In general, the current owner may take any player that has not been taken previously. Once all owners have selected one player, they repeat this process until all owners have selected k players. No player may be selected by multiple teams.</p>

<p>Initially, all players are given a ranking based on how well they played in the previous year. However, the owners may not agree with this order. For example, the first owner may believe that the player which was ranked third in the previous year is the best player and would prefer to take them.</p>

<p>Each owner has a preference list. On their turn, the owner selects the player that is the highest available player on their own preference list. If all players on their preference list are taken, then they resort to using the ordering from the previous year.</p>

<p>Given the preference list of each owner and the rankings from the previous year, which players did each owner get?</p>

### 입력 

 <p>The first line of the input contains two integers n (1 ≤ n ≤ 60), the number of owners, and k (1 ≤ k ≤ 1 000), the size of each team.</p>

<p>The next n lines contain owners’ preferences in the order of drafting. Each line starts with an integer q<sub>i</sub> (0 ≤ q<sub>i</sub> ≤ 1 500), the size of the i<sup>th</sup> owners’ preference list. q<sub>i</sub> names follow, separated by spaces, in order of i<sup>th</sup> owner’s preference. No name appears more than once in the i<sup>th</sup> owners’ list.</p>

<p>The next line contains a single integer p (n · k ≤ p ≤ 65 000), indicating the number of players in the draft.</p>

<p>The next p lines each contain a single name, they are ordered by their previous year’s ranking. Each player name is unique and comprised of at most 12 letters of English alphabet.</p>

<p>The names in owners’ preference lists are guaranteed to appear in the player list.</p>

### 출력 

 <p>Display n lines. The i<sup>th</sup> of which contains the k names of the players that were selected by the i<sup>th</sup> owner. The n teams should be in the original order of owners and players should be listed in the order in which they were drafted following the rules above.</p>

