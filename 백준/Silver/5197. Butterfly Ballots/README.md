# [Silver I] Butterfly Ballots - 5197 

[문제 링크](https://www.acmicpc.net/problem/5197) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 8월 9일 23:31:32

### 문제 설명

<p>To “properly” improve one’s chances for winning an election, it is helpful to have allies on the election board. For instance, it can be quite useful to have the ballot designed in such a way that voters who are not paying close attention may actually vote for the wrong candidate. One tried and true way to achieve that is the so-called “Butterfly Ballot”. In a butterfly ballot, all the candidates’ names are on one side (say, the left), while all the boxes in which to mark a vote are on the other side. Now, if the boxes are a little bit shifted, it can be hard to tell which box corresponds to which candidate. For instance, look at the following ballot:</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/ballot.png" style="height:228px; width:602px"></p>

<p>You’ll have to admit that if one isn’t careful with this ballot, one might easily end up making a mark next to UCLA instead of USC. Of course, similar things could happen to political candidates.</p>

<p>You are to write a program to design a ballot that will make your candidate win, if possible. The assumption is that all candidates must be on the ballot, in some order from top to bottom that you can determine. The boxes will be on the other side, so that the first box is above the first candidate, the second box between the first and second candidate, and so forth. The assumption is then that among the voters who intend to vote for candidate i, half will actually vote for i, and half will accidentally vote for candidate i + 1. Of course, among the voters who intend to vote for the last candidate on the ballot, all will vote correctly. You are to decide if your candidate can be made to win the election. (If your candidate is tied for first place, we also consider that a win.)</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of the data set contains a number n with 1 ≤ n ≤ 100, the number of candidate on the ballot. Candidate 1 is the one you are trying to make win. This is followed by n lines, each containing a number vi, the number of voters who intend to vote for candidate i. All the vi will be even numbers, so you don’t need to worry about what happens about division by 2.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. If it is possible for candidate 1 to win, then output “Possible” on a line by itself, otherwise output “Impossible”.</p>

