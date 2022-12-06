# [Bronze I] Time Cards - 6122 

[문제 링크](https://www.acmicpc.net/problem/6122) 

### 성능 요약

메모리: 28776 KB, 시간: 112 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Farmer John wanted to improve farm productivity, so his cows now get extra hay if they spend more time at a milking machine. To implement this plan, he has instituted the use of time cards for each of the N (1 <= N <= 145) cows conveniently numbered 1..N. When a cow starts at a milking machine, she enters the start time on the master time card. Likewise, when she leaves, she notes that on the master time card, as well. FJ is fortunate to have enough milking machines that he can milk every cow at the same time.</p>

<p>The time entries are typed into a computer file where each line includes a cow number C (1 <= C <= N), a keyword ('START' or 'STOP'), and the time expressed as two space-separated integers HH and MM (0 <= HH <= 23; 0 <= MM <= 59). Cows never stay at the machine past midnight. The timecard file is complete in the sense that every cow's START entry contains a corresponding STOP entry later in the input file.</p>

<p>Calculate the total time each cow spends at the milking machine.</p>

<p>By way of example, consider a time card file for just two cows. The file includes not only the number of cows but also the total number of time card entries, Nlines (1 <= Nlines <= 1,458).</p>

<pre>2 6
1 START 9 0
2 START 9 30
1 STOP 10 0
2 STOP 10 15
1 START 17 0
1 STOP 17 42</pre>

<p>Cow 1 spent times 9:00-10:00 and 17:00-17:42 at the machine for a total of one hour and 42 minutes (1:42). Cow 2 spent time 9:30-10:15 at the machine, for a total of 45 minutes.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and Nlines</li>
	<li>Lines 2..Nlines+1: Each line contains four space-separated entities: C, keyword, HH, and MM</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..N: Line i contains two space-separated integers that are respectively the number of hours and minutes that cow i spends at the milking machine. Of course, the minutes value never exceeds 59.</li>
</ul>

<p> </p>

