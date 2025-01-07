# [Silver II] It’s tough being a teen! - 6858 

[문제 링크](https://www.acmicpc.net/problem/6858) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

브루트포스 알고리즘, 방향 비순환 그래프, 그래프 이론, 위상 정렬

### 제출 일자

2025년 1월 8일 01:55:29

### 문제 설명

<p>There is always a list of things to be done!</p>

<p>Here is a list for you left just this morning by your parental figure.</p>

<ol>
	<li>Do your Math homework.</li>
	<li>Call your grandma.</li>
	<li>Call me at work.</li>
	<li>Call your friend.</li>
	<li>Feed the dog.</li>
	<li>Let the dog out.</li>
	<li>Watch television.</li>
</ol>

<p>(It is nice that your parental figure makes sure you watch television, and not just use the internet all day long.)</p>

<p>As well, your parental figure has given you constraints on these tasks:</p>

<ul>
	<li>Do your Math homework BEFORE you watch Television.</li>
	<li>Do your Math homework BEFORE you call your friend.</li>
	<li>Call your grandma BEFORE you do your Math homework.</li>
	<li>Call me at work BEFORE you call your friend.</li>
	<li>Feed the dog AFTER you call me at work.</li>
</ul>

<p>Your “to do” list (above) can now be abbreviated to:</p>

<pre>1,7
1,4
2,1
3,4
3,5
</pre>

<p>where x, y indicates that the task numbered x should be done before the task numbered y.</p>

<p>Unfortunately, during the day additional instructions are emailed to you by your parental figure. Write a program to use your original “to do” list and the additional instructions to output a list of your jobs in the order you must do them, or alternately, if you cannot complete them, you should output that there is no way to complete these tasks, and you are just going to go to bed.</p>

### 입력 

 <p>You will be given pairs of numbers, one number per line, to represent the additional instructions to be included with your original “to do” list given above. The data terminates with the input pair 0 and 0. You can assume that there will be at most 10 additional constraints.</p>

### 출력 

 <p>You should output a list of tasks in the order that they should be performed, or an error message saying that the tasks cannot be completed. If there are multiple orders in which the tasks may be completed, the following tie-breaking rule must be used:</p>

<p>If there is a set of tasks which may be performed at the same time during the process, the smallest numbered task should be performed first.</p>

