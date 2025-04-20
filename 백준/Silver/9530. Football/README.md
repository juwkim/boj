# [Silver I] Football - 9530 

[문제 링크](https://www.acmicpc.net/problem/9530) 

### 성능 요약

메모리: 114788 KB, 시간: 120 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 4월 20일 20:34:20

### 문제 설명

<p>Your favorite football team is playing a charity tournament, which is part of a worldwide fundraising effort to help children with disabilities. As in a normal tournament, three points are awarded to the team winning a match, with no points to the losing team. If the game is drawn, each team receives one point.</p>

<p>Your team played N matches during the first phase of the tournament, which has just finished. Only some teams, the ones with more accumulated points, will advance to the second phase of the tournament. However, as the main objective of the tournament is to raise money, before the set of teams that will pass to the second phase is determined, each team is allowed to buy additional goals. These new goals count as normally scored goals, and may be used to alter the result of any of the matches the team played.</p>

<p>Your team’s budget is enough to buy up to G goals. Can you tell the maximum total number of points your team can get after buying the goals, supposing the other teams will not buy any goals?</p>

### 입력 

 <p>The first line contains two integers N (1 ≤ N ≤ 10<sup>5</sup>) and G (0 ≤ G ≤ 10<sup>6</sup>) representing respectively the number of matches your team played and the number of goals your team can buy. Each of the next N lines describes a match result with two integers S and R (0 ≤ S, R ≤ 100), indicating respectively the goals your team scored and received on that match before buying goals.</p>

### 출력 

 <p>Output a line with an integer representing the maximum total number of points your team can get after buying the goals.</p>

