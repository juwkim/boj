# [Bronze II] Haughty Cuisine - 20336 

[문제 링크](https://www.acmicpc.net/problem/20336) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>As a waiter, your favourite question from an indecisive punter is "I'm not sure, what would you recommend?" --- so much so, in fact, that you decided to automate away the answer to avoid having to spend any brain cycles on this question ever again.</p>

<p>You have the list of all set menus for today and you are going to simply pick one at random. As long as your recommendation corresponds to a list of items on a set menu, everything will be fine.</p>

### 입력 

 <ul>
	<li>One line containing a single integer $1\leq n\leq 100$, the number of set menus.</li>
	<li>$n$ lines, one for each menu. Each of these lines contains a single integer $1\leq d\leq 42$, followed by a list of $d$ dishes that the meal consists of.</li>
</ul>

<p>Each dish is described using at most $20$ lowercase Latin characters.</p>

### 출력 

 <p>Output one line containing $m$, the number of dishes that you recommend, followed by $m$ lines containing the dishes you recommend.</p>

<p>If there are multiple possible solutions, you may output any one of them.</p>

