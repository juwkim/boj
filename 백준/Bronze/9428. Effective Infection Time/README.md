# [Bronze II] Effective Infection Time - 9428 

[문제 링크](https://www.acmicpc.net/problem/9428) 

### 성능 요약

메모리: 113112 KB, 시간: 124 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>You are estimating the threat level of quarantined zones that have been abandoned to the infection. One of the key variables in determining a zone's threat level is the EIT (Effective Infection Time). This information is essential for planning strike dates to reclaim quarantined zones. The EIT is calculated according to the following rules:</p>

<ul>
	<li>The EIT is the result of a function of two dates: The infection date and the strike date.</li>
	<li>All years are in A.Z. (After Zombie).</li>
	<li>Every month counts for a fraction of an EIT after its last day has passed. This means the month of the strike date does not count for EIT.</li>
	<li>The first calendar year of the infection is calculated as 1/2 EIT.
	<ul>
		<li>If the end of the year is not reached, each month only counts for a fraction of the 1/2 EIT. If a zone was infected in January of the first year, then the 1/2 EIT is spread across 12 months ((1/2)/12 = ~ 0.0417 EIT per month). If a zone was infected in March of the first year, then the 1/2 EIT is spread across 10 months ((1/2)/10 = 0.0500 EIT per month).</li>
		<li>If the end of the year is reached, the year counts as a full 1/2 EIT, regardless of the infection month. In other words, a zone infected in February of 15 A.Z. counts as only 1/2 (one-half) EIT after December 15 A.Z. A zone infected in December of the same year will also count as 1/2 EIT.</li>
	</ul>
	</li>
	<li>All following years are calculated as 1 EIT. Each calendar month, beginning with January, counts for 1/12 EIT (~ 0.0833 EIT).</li>
	<li>Every zone infected on the same month will have the same EIT for any given strike date. Therefore only the month and year are given.</li>
</ul>

<p>The number and order of months in a calendar year remains the same as the modern Gregorian calendar.</p>

### 입력 

 <p>The first line will be an integer N, where 1 <= N <= 50 giving the number of zones. For each zone, a pair of lines of will be provided:</p>

<ul>
	<li>The first line contains the infection date. The second contains the strike date.</li>
	<li>The first integer of a date represents the month, M (1 <= M <= 12), and the second integer represents the year, Y (0000 <= Y <= 0030). The year will always have 4 digits.</li>
	<li>The strike date will never precede the infection date.</li>
</ul>

### 출력 

 <p>Output the EIT for each zone on its own line. The EIT must be rounded to the fourth digit after the decimal point. The ones-digit must always be printed even if it is a zero.</p>

