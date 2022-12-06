# [Bronze I] Gerrymandering - 17587 

[문제 링크](https://www.acmicpc.net/problem/17587) 

### 성능 요약

메모리: 29028 KB, 시간: 484 ms

### 분류

구현(implementation)

### 문제 설명

<p>Electoral systems across the world can vary widely. In some systems, such as <em>winner-take-all</em>, the winner is determined by the plurality of votes—the candidate that receives the most votes wins, and the loser(s) do not get a position.</p>

<p>Such elections can have “wasted votes.” Conceptually, a wasted vote is a vote that did not affect the election outcome. While the exact definition of a wasted vote varies, we’ll adopt the following definition: in an election with <em>V</em> voters, every vote for a losing candidate is wasted (these are called <em>lost votes</em>), and every vote for a winning candidate beyond the strict majority of ⌊<em>V</em> /2⌋ + 1 votes the candidate needs to win is wasted (these are called <em>excess votes</em>). For this problem we’ll consider a two-party system (let’s call the parties A and B) with elections that always involve one candidate from each party.</p>

<p>Let’s illustrate wasted votes with a simple example between two candidates in a district. Suppose that the candidate for party A receives 100 votes and the candidate for party B receives 200 votes. All 100 votes for party A are wasted (lost votes for A), and 49 votes for party B are wasted (excess votes for B). This is because B needs 151 (⌊(100 + 200)/2⌋ + 1) votes to win (over A), so the remaining 49 are wasted.</p>

<p>Political scientists use wasted votes to compute the <em>efficiency gap</em>, a single number that summarizes wasted votes. Suppose we have a number of races in different districts, where each district elects one person. Across all districts there are <em>V</em> total votes cast, with <em>w<sub>A</sub></em> total wasted votes for party A and <em>w<sub>B</sub></em> total wasted votes for party B. Then the efficiency gap is:</p>

<p style="text-align: center;"><em>E</em>(<em>V</em>, <em>W<sub>A</sub></em>, <em>W<sub>B</sub></em>) = |<em>W<sub>A</sub></em> - <em>W<sub>B</sub></em>| / <em>V</em> .</p>

<p>A low efficiency gap indicates that the elections are competitive, and that the number of candidates elected from each party is representative of the total voting share for each party. When the efficiency gap is high, this can be an indication of <em>gerrymandering</em>. Gerrymandering refers to organizing voting districts in a way that favors a particular political outcome. Two common ways of doing this are to “pack” similar voters into districts, or “crack” them across multiple districts; both ways tend to diminish those voters’ influence in electing candidates they would like to win.</p>

<p>In an election, districts are made up of precincts. A precinct is an indivisible group of voters. The votes for all precincts in a district are added together to find the results for that district. In this problem you are given a description of a number of precincts: the party vote totals for each precinct, and how those precincts have been grouped into districts. For each district, determine the party that wins and the wasted votes for each party. Then determine the efficiency gap between the two parties over all the districts.</p>

### 입력 

 <p>The input describes one election. The first line contains two integers <em>P</em> and <em>D</em>, where 1 ≤ <em>P</em> ≤ 10 000 and 1 ≤ <em>D</em> ≤ min(1 000, <em>P</em>). These indicate, respectively, the number of voting precincts and districts. Following this are <em>P</em> lines describing the precincts. Line <em>i</em> contains 3 numbers: the district <em>d<sub>i</sub></em> that precinct <em>i</em> is assigned to (1 ≤ <em>d<sub>i</sub></em> ≤ <em>D</em>), the number of votes for the candidate from party A (0 ≤ <em>a<sub>i</sub></em> ≤ 100 000), and the number of votes for the candidate from party B (0 ≤ <em>b<sub>i</sub></em> ≤ 100 000). It is guaranteed that:</p>

<ul>
	<li>for each precinct <em>i</em>, 0 < <em>a<sub>i</sub></em> + <em>b<sub>i</sub></em>,</li>
	<li>each district is assigned at least one precinct, and</li>
	<li>there are no ties within any district.</li>
</ul>

### 출력 

 <p>For each of the districts from 1 to <em>D</em>, print which party wins (a single character, either <em>A</em> or <em>B</em>). Then print the number of wasted votes for party A and for party B, in order. Finally, after reporting on all the districts, print the efficiency gap as measured over all the districts. The efficiency gap should be accurate to within an absolute error of 10<sup>−6</sup>.</p>

