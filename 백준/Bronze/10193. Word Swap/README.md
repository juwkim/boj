# [Bronze II] Word Swap - 10193 

[문제 링크](https://www.acmicpc.net/problem/10193) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

문자열(string)

### 문제 설명

<p>Agnes has heard that the carnival is going to have a new game next year. The carnival guy chooses a word and writes it down on a piece of paper, and only tells you the length of the word (lets call it Word 1). You have to guess a word of the same length (lets call it Word 2), and you earn or lose coins depending on how different are the two words (i.e., based on how much effort is required to swap the two words). Agnes, having just turned 6, has barely started reading and can’t do math yet, so she wants your help to play this game.</p>

<p>The carnival provided the following rules for earning or paying coins.</p>

<ul>
	<li>Only letters a-z will be used in the game.</li>
	<li>The difference between words is decided on a position-by-position basis.</li>
	<li>For each position: (1) if the characters in that position in the two words are the same, no coins are paid or earned; (2) if the character in Word 1 at that position appears alphabetically before the character in Word 2, then you have to pay 1 coin for each character between the two characters and 1 additional coin; (3) if the character in Word 1 at that position appears alphabetically after the character in Word 2, then you earn 1 coin for each character between the two characters and 1 additional coin.</li>
</ul>

<p>For example: if the carnival guy wrote down agnes and you guessed heard, then the following table shows the calculation.</p>

<table class="table table-bordered" style="width: 100%;">
	<thead>
		<tr>
			<th> </th>
			<th>Position 1</th>
			<th>Position 2</th>
			<th>Position 3</th>
			<th>Position 4</th>
			<th>Position 5</th>
			<th>Total</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>Carnival Word</th>
			<td>a</td>
			<td>g</td>
			<td>n</td>
			<td>e</td>
			<td>s</td>
			<td> </td>
		</tr>
		<tr>
			<th>Your Word</th>
			<td>h</td>
			<td>e</td>
			<td>a</td>
			<td>r</td>
			<td>d</td>
			<td> </td>
		</tr>
		<tr>
			<th>Coins</th>
			<td>paid 7</td>
			<td>earned 2</td>
			<td>earned 13</td>
			<td>paid 13</td>
			<td>earned 15</td>
			<td><u>earned 10</u></td>
		</tr>
	</tbody>
</table>

<ul>
	<li>You might think this is not particularly interesting game, since one can always guess words like “aal”, “abut”, etc. (depending on length), and easily earn coins. However, there is a twist: if it turns out you would earn too many coins, you don’t earn anything (its a carnival game after all). We will ignore this twist.</li>
</ul>

<p>You have to write a program that tells Agnes how many coins she will earn or have to pay for a pair of words. The program will read in a series of pairs of words and report the amount paid or earned. The provided skeleton handles the input of the words and the output messages. You need to implement the method costToSwap which returns an integer.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases. After that each line will contain two words separated by a space.</p>

### 출력 

 <p>For each test case, the program will display the number of coins paid or earned.</p>

