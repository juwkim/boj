# [Silver II] gRanks (Small) - 12058 

[문제 링크](https://www.acmicpc.net/problem/12058) 

### 성능 요약

메모리: 110064 KB, 시간: 108 ms

### 분류

구현, 정렬

### 제출 일자

2025년 1월 10일 05:04:06

### 문제 설명

<p>There are many great athletes in the world, and it's very hard to say who is the best in the world at a particular sport, especially when different athletes have won different competitions. Here's one possible system for ranking athletes:</p>

<ol>
	<li>Determine the number <strong>P</strong> of finishing places in any competition that will be worth points for athletes, and how many points <strong>S<sub>i</sub></strong> each of those finishing places is worth. For example, for <strong>P</strong> = 3, one possible assignment would be 1000 points for 1st place, 500 for 2nd place, and 300 for 3rd place, and 0 for anything below that. (We assume there are no ties within competitions.)</li>
	<li>Since not all competitions are equally important, assign a weight <strong>W<sub>i</sub></strong> to each one. The score gained by an athlete for a competition will be the points from step 1, modified by the weight for that competition. For example, we may decide that Olympics has a weight of 5, and, continuing with our example from above, the winner of the Olympics would receive 5 * 1000 = 5000 points.</li>
	<li>Since we don't want to reward athletes simply for participating in many competitions, we count only the <strong>M</strong> highest scores received by an athlete across all competitions. For example, if <strong>M</strong> = 2 and an athlete earns scores of 1000*5, 500*1, and 300*3 in three different competitions, only the 5000 and 900 would be counted.</li>
</ol>

<p>You are given the points per finishing place, the weights of the competitions, and the results of the competitions. Can you rank all of the athletes who appeared in the competitions? If multiple athletes have the same score, they will share the same rank and listed in alphabetical order of their names.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow; each test case consists of the following:</p>

<ol>
	<li>One line with an integer <strong>P</strong>, the number of top places for which points are awarded.</li>
	<li>One line consists with <strong>P</strong> integers representing the scores <strong>S<sub>i</sub></strong> for the top places, starting with first place and continuing down the places.</li>
	<li>One line with an integer <strong>N</strong>, the number of competitions.</li>
	<li><strong>N</strong> lines, each of which represents a competition. Each line begins with <strong>W<sub>i</sub></strong>, the weight of this competition, and continues with the <strong>P</strong> names of the athletes who finished in the top <strong>P</strong> places. They are listed in descending order starting from first place.</li>
	<li>One line with an integer <strong>M</strong>, the maximum number of competitions counted toward an athlete's score.</li>
</ol>

### 출력 

 <p>For each test case, output one line containing "Case #x:", where x is the test case number (starting from 1). Then output one line for each athlete, from highest rank to lowest rank, with the format <code>r: name</code>, where <code>r</code> is the rank of the athlete and <code>name</code> is the name of the athlete. You need to rank all of the athletes that appeared in the input.</p>

