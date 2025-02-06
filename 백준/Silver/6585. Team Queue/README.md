# [Silver II] Team Queue - 6585 

[문제 링크](https://www.acmicpc.net/problem/6585) 

### 성능 요약

메모리: 116652 KB, 시간: 176 ms

### 분류

자료 구조, 구현, 큐, 시뮬레이션

### 제출 일자

2025년 2월 7일 07:21:57

### 문제 설명

<p><em>Queues</em> and <em>Priority Queues</em> are data structures which are known to most computer scientists. The <em>Team Queue</em>, however, is not so well known, though it occurs often in everyday life. At lunch time the queue in front of the Mensa is a team queue, for example.</p>

<p>In a team queue each element belongs to a team. If an element enters the queue, it first searches the queue from head to tail to check if some of its <em>teammates</em> (elements of the same team) are already in the queue. If yes, it enters the queue right behind them. If not, it enters the queue at the tail and becomes the new last element (bad luck). Dequeuing is done like in normal queues: elements are processed from head to tail in the order they appear in the team queue.</p>

<p>Your task is to write a program that simulates such a team queue.</p>

### 입력 

 <p>The input file will contain one or more test cases. Each test case begins with the number of teams t (1 ≤ t ≤ 1000). Then t team descriptions follow, each one consisting of the number of elements belonging to the team and the elements themselves. Elements are integers in the range 0 - 999999. A team may consist of up to 1000 elements.</p>

<p>Finally, a list of commands follows. There are three different kinds of commands:</p>

<ul>
	<li>ENQUEUE x - enter element x into the team queue</li>
	<li>DEQUEUE - process the first element and remove it from the queue</li>
	<li>STOP - end of test case</li>
</ul>

<p>The input will be terminated by a value of 0 for <em>t</em>.</p>

<p>Warning: A test case may contain up to 200000 (two hundred thousand) commands, so the implementation of the team queue should be efficient: both enqueing and dequeuing of an element should only take constant time.</p>

### 출력 

 <p>For each test case, first print a line saying "Scenario #<em>k</em>", where <em>k</em> is the number of the test case. Then, for each DEQUEUE command, print the element which is dequeued on a single line. Print a blank line after each test case, even after the last one.</p>

