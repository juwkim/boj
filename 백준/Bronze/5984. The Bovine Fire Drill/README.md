# [Bronze I] The Bovine Fire Drill - 5984 

[문제 링크](https://www.acmicpc.net/problem/5984) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>The N (3 <= N <= 250) cows (conveniently labeled cow_1..cow_N) sat in a perfect circle  around the camp fire in chairs numbered chair_1..chair_N as Farmer John told them stories of the old days (cow_i sits in chair_i, of course). At the conclusion of one story, FJ suggested they perform a Bovine Fire Drill.</p>

<p>In a Bovine Fire Drill, one cow at a time walks around the circle from her chair to a potentially new chair while the other cows chant "Fire, fire, fire." When it is cow_i's turn to move, she rises and moves clockwise to the i'th chair encountered in that direction (so if it was cow_3's turn, she would rise from chair_3 and move to chair_6 if N >= 6).</p>

<p>When cow_i arrives at her new chair, she taps any cow sitting there on the shoulder; that cow rises to make room for cow_i, who sits down. This process continues until a cow lands in an empty chair or until a cow is asked to move for a second time. In either of those cases, the game ends. Cow 1 always starts, so it is her chair that will be the empty one.</p>

<p>Only rarely do all the cows get to participate, as the game termination conditions arise naturally and frequently from the properties of whole numbers. The final cow to move (whether she ends the game by sitting in cow_1's chair or by tapping the shoulder of a cow who has already moved) receives a special treat of extra tender grass.</p>

<p>Help FJ plan in advance to learn which cow will get the tender grass.</p>

<p>For example, consider five cows sitting around the blazing campfire:</p>

<pre>  2   -   3
 (         )
  1 - 5 - 4</pre>

<p>First, cow 1 walks one space and taps cow 2, who rises. (The * denotes the empty chair.)</p>

<pre>    2
 1   -   3
 (         )
  * - 5 - 4</pre>

<p>Cow 2 walks two spaces and taps cow 4, who begins her journey:</p>

<pre>  1  -    3
 (         )
  * -  5 - 2
          4</pre>

<p>Cow 4 will walk four spaces and tap cow 3:</p>

<pre>             3
  1   -    4  
 (         )
  * -  5 - 2</pre>

<p>Finally, cow 3 will walk three spaces to chair_1, which is empty and thus terminates the drill.</p>

<pre>  1   -    4  
 (         )
  3 -  5 - 2</pre>

<p>Cow 3 receives tender spring grass as the other cows clap and cheer.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The number of the cow who ends the drill</li>
</ul>

<p> </p>

