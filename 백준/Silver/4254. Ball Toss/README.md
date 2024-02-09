# [Silver III] Ball Toss - 4254 

[문제 링크](https://www.acmicpc.net/problem/4254) 

### 성능 요약

메모리: 109240 KB, 시간: 116 ms

### 분류

구현

### 제출 일자

2024년 2월 9일 22:15:34

### 문제 설명

<p>Classmates stand in a circle facing inward, each with the direction left or right in mind. One of the students has a ball and begins by tossing it to another student. (It doesn’t really matter which one.) When one catches the ball and is thinking left, she throws it back across the circle one place to the left (from her perspective) of the person who threw her the ball. Then she switches from thinking left to thinking right. Similarly, if she is thinking right, she throws the ball to the right of the person who threw it to her and then switches from thinking right to thinking left.</p>

<p>There are two exceptions to this rule: If one catches the ball from the classmate to her immediate left and is also thinking left, she passes the ball to the classmate to her immediate right, and then switches to thinking right. Similarly, if she gets the ball from the classmate to her immediate right and is thinking right, she passes the ball to the classmate to her immediate left, and then switches to thinking left. (Note that these rules are given to avoid the problem of tossing the ball to oneself.)</p>

<p>No matter what the initial pattern of left and right thinking is and who first gets tossed the ball, everyone will get tossed the ball eventually! In this problem, you will figure out how long it takes.</p>

<p>You’ll be given the initial directions of n classmates (numbered clockwise), and the classmate to whom classmate 1 initially tosses the ball. (Classmate 1 will always have the ball initially.)</p>

### 입력 

 <p>There will be multiple problem instances. Each problem instance will be of the form</p>

<pre>n k t<sub>1</sub> t<sub>2</sub> t<sub>3</sub> ... t<sub>n</sub></pre>

<p>where n (2 ≤ n ≤ 30) is the number of classmates, numbered 1 through n clockwise around the circle, k (> 1) is the classmate to whom classmate 1 initially tosses the ball, and t<sub>i</sub> (i = 1, 2,...,n) are each either L or R, indicating the initial direction thought by classmate i. (n = 0 indicates end of input.)</p>

### 출력 

 <p>For each problem instance, you should generate one line of output of the form:</p>

<pre>Classmate m got the ball last after t tosses.</pre>

<p>where m and t are for you to determine. You may assume that t will be no larger than 100,000.</p>

<p>Note that classmate number 1 initially has the ball and tosses it to classmate k. Thus, number 1 has not yet been tossed the ball and so does not switch the direction he is thinking.</p>

