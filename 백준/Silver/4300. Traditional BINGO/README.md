# [Silver IV] Traditional BINGO - 4300 

[문제 링크](https://www.acmicpc.net/problem/4300) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Traditional BINGO is played in person in a large hall. Players meet at the hall, pay a fee to get in, then the games begin. A night of BINGO consists of many BINGO games played continuously, one after another.</p>

<p>A single BINGO game proceeds like this: Each player has a number of BINGO cards (players can usually play any number of cards). Each BINGO card has 5 rows and 5 columns thus providing 25 spaces.</p>

<p>The columns are labeled from left to right with the letters: 'B', 'I', 'N', 'G', 'O'. With one exception (the center space is "free") the spaces in the card are assigned values as follows:</p>

<ul>
	<li>Each space in the 'B' column contains a number from 1 - 15.</li>
	<li>Each space in the 'I' column contains a number from 16 - 30.</li>
	<li>Each space in the 'N' column contains a number from 31 - 45.</li>
	<li>Each space in the 'G' column contains a number from 46 - 60.</li>
	<li>Each space in the 'O' column contains a number from 61 - 75.</li>
</ul>

<p>Furthermore, a number can appear only once on a single card.</p>

<p>Here's a sample BINGO card:</p>

<table class="table table-bordered" style="width:30%">
	<thead>
		<tr>
			<th style="width:6%">B</th>
			<th style="width:6%">I</th>
			<th style="width:6%">N</th>
			<th style="width:6%">G</th>
			<th style="width:6%">O</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>10</td>
			<td>17</td>
			<td>39</td>
			<td>49</td>
			<td>64</td>
		</tr>
		<tr>
			<td>12</td>
			<td>21</td>
			<td>36</td>
			<td>55</td>
			<td>62</td>
		</tr>
		<tr>
			<td>14</td>
			<td>25</td>
			<td>FREE<br>
			SPACE</td>
			<td>52</td>
			<td>70</td>
		</tr>
		<tr>
			<td>7</td>
			<td>19</td>
			<td>32</td>
			<td>56</td>
			<td>68</td>
		</tr>
		<tr>
			<td>5</td>
			<td>24</td>
			<td>34</td>
			<td>54</td>
			<td>71</td>
		</tr>
	</tbody>
</table>

<p>The number of unique BINGO cards is very large and can be calculated with this equation:</p>

<pre>// the B, I, G, and O columns * the N column
(15 * 14 * 13 * 12 * 11) ^ 4 * (15 * 14 * 13 * 12)</pre>

<p>While perhaps interesting to a statistician, the number of possible BINGO cards has nothing to do with player's chances of winning.</p>

<p>You will note that there are 75 possible BINGO numbers:</p>

<pre>B1, B2, B3, ... B15, I16, I17, I18, ... I30, N31, N32, ... O74, O75.</pre>

<p>Each of these numbers is represented by a ball in a large rotating bin. Each ball is painted with its unique BINGO number. An announcer spins the bin, reaches in a selects a ball, and a announces it to the room. The players check all of their cards to see if that number appears on their card. If it is, they mark it. A player may mark the centre FREE SPACE at any time.</p>

<p>When a player has a BINGO (5 marks in a row, column, or diagonal), he or she calls out BINGO. The game pauses while the card is verified. If indeed a winner, the game stops and a new game begins. If the card wasn't a winner, the game proceeds where it left off. Each BINGO game proceeds until someone wins (there's always a winner).</p>

### 입력 

 <p>The first line of input contains n, the number of BINGO games that you will analyze. n game descriptions follow. Each game description specifies a card to be played followed by a sequence of BINGO numbers. You are to determine, when the holder of the card will win the game, assuming the player has just this one card and there are no other players.</p>

### 출력 

 <p>Each card description consists of five lines, giving the numbers on the card row by row. All but the 3rd row contain 5 numbers; the 3rd contains 4 because of the free space. One or more lines follow that represent some ordering of all 75 bingo numbers. All bingo numbers are simply integers between 1 and 75 - the one-letter prefix is redundant. For each game, ouput the line "BINGO after n numbers announced" as appropriate.</p>

