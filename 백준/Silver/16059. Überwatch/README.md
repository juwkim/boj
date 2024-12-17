# [Silver II] Überwatch - 16059 

[문제 링크](https://www.acmicpc.net/problem/16059) 

### 성능 요약

메모리: 164084 KB, 시간: 164 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 12월 17일 20:40:13

### 문제 설명

<p>The lectures are over, the assignments complete and even those pesky teaching assistants have nothing left to criticize about your coding project. Time to play some video games! As always, your procrastinating self has perfect timing: Cold Weather Entertainment just released Überwatch, a competitive first person video game!</p>

<p>Sadly, you aren’t very good at these kind of games. However, Überwatch offers more than just skill based gameplay. In Überwatch you can defeat all opponents in view with a single button press using your ultimate attack. The drawback of this attack is that it has to charge over time before it is ready to use. When it is fully charged you can use it at any time of your choosing. After its use it immediately begins to charge again.</p>

<p>With this knowledge you quickly decide on a strategy:</p>

<ul>
	<li>Hide from your opponents and wait for your ultimate attack to charge.</li>
	<li>Wait for the right moment.</li>
	<li>Defeat all opponents in view with your ultimate attack.</li>
	<li>Repeat.</li>
</ul>

<p>After the game your teammates congratulate you on your substantial contribution. But you wonder: How many opponents could you have defeated with optimal timing?</p>

<p>The game is observed over n time slices. The ultimate attack is initially not charged and requires m time slices to charge. This first possible use of the ultimate attack is therefore in the (m+1)-th time slice. If the ultimate attack is used in the i-th time slice, it immediately begins charging again and is ready to be fired in the (i + m)-th time slice.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with two integers n and m, where
	<ul>
		<li>n (1 ≤ n ≤ 300 000) is the game duration;</li>
		<li>m (1 ≤ m ≤ 10) is the time needed to charge the ultimate attack in time slices.</li>
	</ul>
	</li>
	<li>one line with n integers x<sub>i</sub> (0 ≤ x<sub>i</sub> ≤ 32) describing the number of opponents in view during a time slice in order.</li>
</ul>

### 출력 

 <p>Output the maximum number of opponents you can defeat.</p>

