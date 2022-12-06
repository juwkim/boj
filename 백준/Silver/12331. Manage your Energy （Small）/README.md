# [Silver V] Manage your Energy (Small) - 12331 

[문제 링크](https://www.acmicpc.net/problem/12331) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>You've got a very busy calendar today, full of important stuff to do. You worked hard to prepare and make sure all the activities don't overlap. Now it's morning, and you're worried that despite all of your enthusiasm, you won't have the energy to do all of this with full engagement.</p>

<p>You will have to manage your energy carefully. You start the day full of energy - <strong>E</strong> <a href="http://en.wikipedia.org/wiki/Joule">joules</a> of energy, to be precise. You know you can't go below zero joules, or you will drop from exhaustion. You can spend any non-negative, integer number of joules on each activity (you can spend zero, if you feel lazy), and after each activity you will regain <strong>R</strong> joules of energy. No matter how lazy you are, however, you <strong>cannot</strong> have more than <strong>E</strong> joules of energy at any time; any extra energy you would regain past that point is wasted.</p>

<p>Now, some things (like solving Code Jam problems) are more important than others. For the <strong>i</strong>th activity, you have a value <strong>v</strong><strong><sub>i</sub></strong> that expresses how important this activity is to you. The <em>gain</em> you get from each activity is the value of the activity, multiplied by the amount of energy you spent on the activity (in joules). You want to manage your energy so that your total gain will be as large as possible.</p>

<p>Note that you <em>cannot</em> reorder the activities in your calendar. You just have to manage your energy as well as you can with the calendar you have.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case is described by two lines. The first contains three integers: <strong>E</strong>, the maximum (and initial) amount of energy, <strong>R</strong>, the amount you regain after each activity, and <strong>N</strong>, the number of activities planned for the day. The second line contains <strong>N</strong> integers <strong>v</strong><strong><sub>i</sub></strong>, describing the values of the activities you have planned for today.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">E</strong><span style="line-height:1.6em"> ≤ 5.</span></li>
	<li>1 ≤ <strong>R</strong> ≤ 5.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10.</li>
	<li>1 ≤ <strong>v</strong><strong><sub>i</sub></strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: <strong>y</strong>", where <strong>x</strong> is the case number (starting from 1) and <strong>y</strong> is the maximum gain you can achieve by managing your energy that day.</p>

