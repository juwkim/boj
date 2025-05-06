# [Silver I] Knee problems (Easy) - 27694 

[문제 링크](https://www.acmicpc.net/problem/27694) 

### 성능 요약

메모리: 113896 KB, 시간: 108 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학

### 제출 일자

2025년 5월 6일 18:41:54

### 문제 설명

<p>You wander through a dark dungeon. All around you there are doors of different shapes and colors. You pick one, open it and enter.</p>

<p>“I knew you would come,” said a voice in the dark. You come closer and see an old man with a long white beard sitting on the floor.</p>

<p>“I used to be a problem solver like you,” he says, “but then I took an arrow in the knee.”</p>

<p>“Seriously?” you ask him.</p>

<p>“Well… not really. It’s just what all the kids were saying the last time I saw daylight.”</p>

<p>“So what happened to you?” you ask and sit beside him.</p>

<p>“The truth is, I destroyed my kneecaps on the stairs. When I was younger, I did a lot of programming contests. And in one of them was a really nasty task. I had to determine the number of ways in which one can go up and down a staircase with n steps. Of course, there were some constraints: when going up, you can take two steps at a time, and when going down, you can take up to four steps at once.”</p>

<p>He sighs deeply. “I had no idea how to solve the task, so I found a staircase and attempted to try every possibility. But there were so many of them that I overloaded my knees and now I can’t even walk. So I’m sitting here and still wondering about a solution for that problem. Can you help me to finally put a close on this?”</p>

<p>The staircase consists of n steps. Count the ways of going up and then down the staircase, given the following constraints:</p>

<ul>
	<li>On the way up, you can take either 1 or 2 steps at a time.</li>
	<li>On the way down, you can take 1, 2, 3, or 4 steps at a time.</li>
</ul>

<p>As the actual number of ways can be huge, compute the remainder it gives when divided by 10<sup>9</sup> + 9.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7e069ddf-3115-428e-8573-f5d20fc1cd16/-/preview/"></p>

<p>For example, for n = 5 one valid way of going up and down the staircase looks as follows: Start on the ground, ascend to step 2, continue to step 3, and then go to step 5. Having now reached the top of the staircase, you turn around and walk down, first descending to step 4 and then going directly to the ground (which is, at that moment, 4 steps below).</p>

<p>The figure above shows two valid ways of going up and down the stairs for n = 5. The one described above is shown in red.</p>

### 입력 

 <p>The first line of input contains one integer number t specifying number of test cases. Each test case is preceded by a blank line.</p>

<p>Each test case consists of a single line with the integer n (1 ≤ n ≤ 100,000) – the number of steps.</p>

### 출력 

 <p>For each test case print a single line with one integer – the number of valid paths modulo 10<sup>9</sup> + 9.</p>

