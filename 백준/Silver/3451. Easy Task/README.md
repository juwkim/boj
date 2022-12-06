# [Silver V] Easy Task - 3451 

[문제 링크](https://www.acmicpc.net/problem/3451) 

### 성능 요약

메모리: 116588 KB, 시간: 212 ms

### 분류

구현(implementation)

### 문제 설명

<p>Last year there were a lot of complains concerning the set of problems. Most contestants considered our problems to be too hard to solve. One reason for this is that the team members responsible for the problems are not able to evaluate properly whether a particular problem is easy or hard to solve. (We have created until now so many problems, that all seems quite easy.) Because we want our future contests to be better we would like to be able to evaluate the hardness of our problems after the contest, using the history of submissions. </p>

<p>There are a few statistics that we can use for evaluating the hardness of a particular problem: the number of accepted solutions of the problem, the average number of submissions of the problem and the average time consumed to solve it (as "General rules" of the contest state "the time consumed for a solved problem is the time elapsed from the beginning of the contest to the submittal of the accepted run."). For the latter two statistics we consider only the teams which solved this particular problem. </p>

<p>Needless to say we ask you to write a program that computes aforementioned statistics for all problems. </p>

<p>Write a program that: </p>

<ul>
	<li>reads a history of submissions during an ACM contest, </li>
	<li>computes for each problem the number of accepted solutions of the problem, the average number of submissions and the average time consumed to solve it, </li>
	<li>writes the result.</li>
</ul>

### 입력 

 <p>The first line of the input contains one integer n (1 ≤ n ≤ 2000) being the number of submissions during the contest. Each of the next n lines describes one submission and contains a submission time (measured in seconds from the beginning of the contest), a team identifier, a problem identifier and a result of evaluating the submission separated by single spaces. The submission time is a positive integer not greater then 18000. The team identifier is a non-empty string consisting of at most five small letters or digits. The problem identifier is a capital letter <code>A</code>, <code>B</code>, ..., or <code>I</code>. The result is a capital letter <code>A</code> (the submission is accepted) or <code>R</code> (the submission is rejected). </p>

<p>Submissions are given in nondecreasing order according to submission times and there are 62 teams competing. </p>

<p>Please note that if a problem is accepted all further submission of this problem by the same team are possible but they should not be taken to the statistics. </p>

### 출력 

 <p>The output consists of nine lines. The first line corresponds to problem A, the second line to problem B, and so on. Each line should contain the problem identifier, the number of accepted solutions of the problem, the average number of submissions done by teams that solved that problem and the average time consumed to solve it separated by single spaces. The latter two statistics should be printed only if there was at least one accepted solution of the given problem and should be rounded to two fractional digits (in particular 1.235 should be rounded to 1.23).</p>

<p> </p>

