# [Silver II] Professor Normal (Small1) - 12349 

[문제 링크](https://www.acmicpc.net/problem/12349) 

### 성능 요약

메모리: 112452 KB, 시간: 288 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 3월 17일 20:34:12

### 문제 설명

<p>Professor Normal's three children have been causing trouble at school; so much so that the principal is threatening to expel them. Clearly, Professor Normal has been doing a great job raising the next generation of recruits for the Evil League of Evil. In order to appease the principal, he has agreed to organize a game for all of the students at the school, to teach them valuable life skills. After all, he can't afford to stay at home with the kids -- he has a job to do and a mortgage to pay.</p>

<p>The game is called Don't Lose Your Marbles. The children stand in an M-by-N grid. Each child is given some number of marbles to start. Different children may be given a different number of marbles; this teaches them that life is unfair.</p>

<p>The game then proceeds in turns. On each turn, each child gives out 12 marbles shared equally among his neighbours. Neighbours are the 4 children immediately in front, behind, to the left, and to the right of the child. Some children will have fewer than 4 neighbours, if they happen to be standing on the edges or in the corners of the grid. This exchange teaches the children about sharing.</p>

<p>Any children who do not have at least 12 marbles at the start of a turn are removed from the game before the marble exchange takes place. Their spots will then remain empty until the end of the game, and their neighbours will have fewer neighbours to exchange marbles with. This teaches the children that one must pay to play.</p>

<p>Children who do not have any neighbours are also then removed because they would have no one to exchange marbles with. This teaches them not to be selfish.</p>

<p>At this point, if there are no children left in the game, the game ends. Otherwise, every remaining child has somebody to exchange marbles with, and the game continues. This teaches the children that all things come to an end.</p>

<p>Or do they? Given the initial arrangement of the children and the number of marbles each child has, can you determine how many turns (marble exchanges) will take place? And please do so quickly, if you can. Professor Normal has evil to plan.</p>

<p>More precisely, the game proceeds according to the following algorithm:<br>
 number_of_exchanges = 0<br>
 repeat forever {<br>
   while (any child has < 12 marbles or 0 neighbors) {<br>
     remove all such children from play<br>
   }<br>
   if (there are no children left in play) {<br>
     the game ends<br>
   }<br>
   simultaneously for each child in play {<br>
     the child shares 12 marbles equally among neighbors<br>
   }<br>
   increment number_of_exchanges by 1<br>
 }</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each one starts with a line containing <strong>M</strong> followed by a line containing <strong>N</strong>. The next <strong>M</strong> lines each contain <strong>N</strong> space-separated integers -- the number of marbles for each child in that row of the grid.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100;</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">M</strong><span style="line-height:1.6em"> ≤ 10;</span></li>
	<li>1 ≤ <strong>N</strong> ≤ 10;</li>
	<li>Each child will start with at most 100 marbles.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y turns", where x is the case number (starting from 1) and y is the number of marble exchanges that will take place before the game is over. If the game goes on forever, then instead output a line containing "Case #x: z children will play forever", where z is the number of children who will remain standing in the school's courtyard forever, playing the game.</p>

