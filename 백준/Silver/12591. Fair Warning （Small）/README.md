# [Silver V] Fair Warning (Small) - 12591 

[문제 링크](https://www.acmicpc.net/problem/12591) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

수학(math)

### 문제 설명

<p><em>On our planet, Jamcode IX, three Great Events occurred. They happened 26000, 11000 and 6000 slarboseconds ago. In 4000 slarboseconds, the amount of time since all of those events will be multiples of 5000 slarboseconds, the largest possible amount... and the apocalypse will come.</em></p>

<p>Luckily for you, you live on Jamcode X! The apocalypse came on Jamcode IX less than a year ago. But Jamcode X has a worrying prophecy: "After the moment of reckoning, on the first <em>optimum anniversary</em> of the <strong>N</strong> Great Events, the apocalypse will come. 64 bits will not save you. You have been warned."</p>

<p>The people of Jamcode X are very concerned by this prophecy. All of the Great Events have already happened, and their times have been measured to the nearest slarbosecond; but nobody knows when their <em>optimum anniversary</em> will occur. After studying the diary of a scientist from Jamcode IX, scientists working on the problem have come up with a theory:</p>

<p>The <em>moment of reckoning</em> is now, the moment you solve this problem. At some time <strong>y ≥ 0</strong>slarboseconds from now, the number of slarboseconds since each of the Great Events will be divisible by some maximum number <strong>T</strong>. If you can find the smallest value of <strong>y</strong> that gives this largest possible <strong>T</strong>, that will give you the <em>optimum anniversary</em> when the apocalypse will come.</p>

<p>On Jamcode IX, for example, there were 3 Great Events and they happened 26000, 11000 and 6000 slarboseconds before the moment of reckoning. 4000 slarboseconds later, the amount of time since each event was a multiple of T=5000 slarboseconds, and the apocalypse came.</p>

<p>Your job is to compute the amount of time until the apocalypse comes. But remember the prophecy: even though the people of Jamcode X have been solving problems for two years, and 64-bit integers have always been enough, they might not always be enough now or in the future.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>C</strong>.  <strong>C</strong> lines follow. Each starts with a single integer <strong>N</strong>, which is followed by a space and then <strong>N</strong> space-separated integers <strong>t<sub>i</sub></strong>, the number of slarboseconds since Great Event <strong>i</strong> occurred.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>C</strong> ≤ 100.</li>
	<li><strong>t<sub>i</sub></strong> ≠ <strong>t<sub>j</sub></strong> for some <strong>i</strong>, <strong>j</strong>.</li>
	<li>2 ≤ <strong>N</strong> ≤ 3.</li>
	<li>1 ≤ <strong>t<sub>i</sub></strong> ≤ 10<sup>8</sup>.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and <strong>y</strong> is the minimum number of slarboseconds until <strong>t<sub>i</sub></strong> + <strong>y</strong> is a multiple of the largest possible integer factor <strong>T</strong> for all <strong>i</strong>.</p>

