# [Bronze I] Hotel - 7798 

[문제 링크](https://www.acmicpc.net/problem/7798) 

### 성능 요약

메모리: 30840 KB, 시간: 96 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Indonesia tourism board has just sent a list of available room type of all hotels in Jakarta for teams that will participate in Indonesia Programming Contest 2008. Each record on the list contains:</p>

<ol>
	<li>Hotel name (max. 25 char, alphabet only).</li>
	<li>Bed size (20 – 62).</li>
	<li>Room capacity (1 – 4).</li>
	<li>Number of available room (1 – 50).</li>
	<li>Cost per room (1 – 5,000).</li>
</ol>

<p>To simplify the problem, let’s assume that each hotel will offer only one type of room (which means they will appear only once in the list).</p>

<p>Several participants have submitted their hotel preference to the committee, which consists of:</p>

<ul>
	<li>Prefered bed size, grouped into three categories:
	<ul>
		<li>Type A: bed size 20 – 35</li>
		<li>Type B: bed size 36 – 48</li>
		<li>Type C: bed size 49 - 62</li>
	</ul>
	</li>
	<li>Number of people in their teams (1 – 200).</li>
	<li>Maximum number of person in a room (1 – 4). The number of people in each room will be limited to this number even if the room has more capacity.</li>
</ul>

<p>Based on the data above, write a program to find the cheapest hotel for each team. If there’re more than one cheapest hotels, then choose one with largest bed size. If there’re still more than one, then choose one which come first on the list.</p>

<p>You don’t have to worry about multiple teams assigned at one hotel. What we will do here is only make a suggestion for each team, not a reservation.</p>

### 입력 

 <p>The first line of input contains an integer T, the number of test cases follow.</p>

<p>Each case will begin with two integers N (1 ≤ N ≤ 50) and M (1 ≤ M ≤ 50) the number of available hotel and the number of teams respectively. The next N lines each will contains four integers (bed size, room capacity, number of available room and the price per room) and a string which denotes the hotel’s name. The next M lines each will contains three data: bed size type (A, B or C), number of people in their teams and maximum number of person in a room.</p>

### 출력 

 <p>Print "Case #X:" (X is the case number) at the first line of each test case. For each team, print on a single line the total cost and the hotel name which you suggested (in the same order as the team appearance in the input), separated by a single space. If there’re no hotels that match the team’s criteria, then output “no-hotel” (without quotes).</p>

