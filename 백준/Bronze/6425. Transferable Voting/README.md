# [Bronze I] Transferable Voting - 6425 

[문제 링크](https://www.acmicpc.net/problem/6425) 

### 성능 요약

메모리: 113112 KB, 시간: 128 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>The Transferable Vote system for determining the winner of an election requires that a successful candidate obtain an absolute majority of the votes cast, even when there are more than two candidates. To achieve this goal, each voter completes his or her ballot by listing <em>all</em> the candidates in order of preference. Thus if there are five candidates for a single position, each voter's ballot must contain five choices, from first choice to fifth choice.</p>

<p>In this problem you are to determine the winner, if any, of elections using the Transferable Vote system. If there are <em>c</em> candidates for the single position, then each voter's ballot will include <em>c</em> distinct choices, corresponding to identifying the voter's first place, second place, ..., and <em>n</em>th place selections. Invalid ballots will be discarded, but their presence will be noted. A ballot is invalid if a voter's choices are not distinct (choosing the same candidate as first and second choice isn't permitted) or if any of the choices aren't legal (that is, in the range 1 to <em>c</em>).</p>

<p>For each election candidates will be assigned sequential numbers starting with 1. The maximum number of voters in this problem will be 100, and the maximum number of candidates will be 5.</p>

<pre><strong>          Table A                Table B</strong>
-----------------------------    -------
<strong>Voter  First   Second  Third
       Choice  Choice  Choice
</strong>  1      1       2       4
  2      1       3       2       1  3  2
  3      3       2       1       3  2  1
  4      3       2       1       3  2  1
  5      1       2       3       1  2  3
  6      2       3       1       3  1
  7      3       2       1       3  2  1
  8      3       1       1
  9      3       2       1       3  2  1
 10      1       2       3       1  2  3
 11      1       3       2       1  3  2
 12      2       3       1       3  1
</pre>

<p>Consider a very small election. In Table A are the votes from the 12 voters for the three candidates. Voters 1 and 8 cast invalid ballots; they will not be counted. This leaves 10 valid ballots, so a winning candidate will require at least 6 votes (the least integer value greater than half the number of valid ballots) to win. Candidates 1 and 3 each have 4 first choice votes, and candidate 2 has two. There is no majority, so the candidate with the fewest first choice votes, candidate 2, is eliminated. If there had been several candidates with the fewest first choice votes, any of them, selected at random, could be selected for elimination.</p>

<p>With candidate 2 eliminated, we advance the second and third choice candidates from those voters who voted for candidate 2 as their first choice. The result of this action is shown in Table B. Now candidate 3 has picked up 2 additional votes, giving a total of 6. This is sufficient for election. Note that if voter 12 had cast the ballot "2 1 3" then there would have been a tie between candidates 1 and 3.</p>

### 입력 

 <p>There will be one or more elections to consider. Each will begin with a line containing the number of candidates and the number of voters, c and n. Data for the last election will be followed by a line containing two zeroes.</p>

<p>Following the first line for each election will be n additional lines each containing the choices from a single ballot. Each line will contain only c non-negative integers separated by whitespace.</p>

### 출력 

 <p>For each election, print a line identifying the election number (they are numbered sequentially starting with 1). If there were any invalid ballots, print an additional line specifying the number of such. Finally, print a line indicating the winner of the election, if any, or indication of a tie; be certain to identify the candidates who are tied. Separate the output for each election by a single blank line.</p>

