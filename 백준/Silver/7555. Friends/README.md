# [Silver V] Friends - 7555 

[문제 링크](https://www.acmicpc.net/problem/7555) 

### 성능 요약

메모리: 34504 KB, 시간: 100 ms

### 분류

많은 조건 분기, 구현, 시뮬레이션

### 문제 설명

<p>You know this problem... several friends meet at the Hacienda (a rather fine restaurant) every Wednesday, have some drinks and fun in general until someone brings up the dreaded question: ”So, where are we going tonight?”</p>

<p>At this point basically two things can happen: Either take the Swedish solution or the Italian solution. The Swedish solution means that there is an absolutely embarrassing silence for about five minutes disturbed only once or twice by a muttered ”Uh, I don’t care...”, then they finally agree (silently of course) to get totally drunk. The Italian solution includes (but is not limited to) lots of shouting, total mayhem in the Hacienda, and probably ’family’ problems.</p>

<p>But wait, yes - you are right. We are in Germany, so our friends will take the German solution, of course. That means: Voting!</p>

<p>As you can imagine, the friends do not just vote for a certain place to go to depending on their current mood. It really depends much more on who is there on a given Wednesday. Here are the rules:</p>

<ol>
	<li>Anne will always vote for going to the cinema.</li>
	<li>Bob will vote for going to the disco if Karin is there, too.</li>
	<li>Karin will vote for going to the disco if Charly is there, if Charly is not there but Anne is, Karin will vote for going to the cinema, if Charly and Anne are not there Karin will vote for going to the cocktail bar.</li>
	<li>Dave is one of those guys who never votes for anything.</li>
	<li>If Dave is there, Bob will vote for going to the cocktail bar.</li>
	<li>If Charly and Anne are there, both of them will vote for going to the cinema.</li>
	<li>Edward votes for going to the cocktail bar if Anne is there and Charly is not there, otherwise Edward votes for going to the cinema.</li>
	<li>If Edward is there, Bob will vote for going to the cocktail bar.</li>
	<li>Frank will vote for going to the cinema if neither Bob nor Anne are there, and Frank will vote for going to the disco if Anne is there.</li>
	<li>If Anne is not there, Bob will vote for going to the cocktail bar.</li>
</ol>

<p>For a given Wednesday, count the votes for each place from the friends who are there on that Wednesday. If no rule applies for a present friend or if several rules apply and require the friend to vote for different places, this friend abstains from voting on that Wednesday</p>

### 입력 

 <p>The first line contains the number of scenarios (Wednesday meetings).</p>

<p>For each scenario, there is one line containing the names of the present friends. Names are separated by single blanks and consist of letters only. The same name will not occur more than once on the same line.</p>

### 출력 

 <p>The output for every scenario begins with a line containing “Scenario #i:”, where i is the number of the scenario starting at 1.</p>

<p>Then for each scenario print a single line containing the place that received the most votes. Possible places are ’cinema’, ’cocktail bar’, and ’disco’. If none of those places receives more votes than the other two print ’stay at the Hacienda’.</p>

<p>Terminate the output for the scenario with a blank line.</p>

