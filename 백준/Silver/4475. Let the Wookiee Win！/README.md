# [Silver V] Let the Wookiee Win! - 4475 

[문제 링크](https://www.acmicpc.net/problem/4475) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘, 구현

### 문제 설명

<p>You are playing against Chewbacca in a tough battle of Galactic Tic-Tac-Toe, which is just like simple Tic-Tac-Toe except that the playing board is 5 × 5 and the goal is to get 4 in a row. In response to a brilliant move, Chewbacca protests loudly and plays his next move, setting you up to win. However, before you can claim victory, Han Solo takes this opportunity to warn you that it’s not wise to upset a Wookiee. After all, they’re known to pull people’s arms out of their sockets when they lose. Wisely, you decide on a new strategy:<strong> Let the Wookiee win!</strong></p>

### 입력 

 <p>Input consists of a series of 5 × 5 playing boards, each separated by a blank line. Each square in a row is separated by a single space. You are ‘O’, Chewie is ‘X’, and empty squares are denoted by ‘*’. For each board, there is exactly one empty square that you can play that does not cause you to win and does not block any of Chewie's winning moves on his next turn. The final board is followed immediately by the word “Finished” on the next line.</p>

### 출력 

 <p><span style="line-height:1.6em">For each board, print a line consisting of the number of the square that you should play to avoid having your arms pulled out of their sockets. The numbering should conform to the following table.</span></p>

<table border="1" cellpadding="1" cellspacing="1" style="width:125px">
	<tbody>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">5</td>
		</tr>
		<tr>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">10</td>
		</tr>
		<tr>
			<td style="text-align: center;">11</td>
			<td style="text-align: center;">12</td>
			<td style="text-align: center;">13</td>
			<td style="text-align: center;">14</td>
			<td style="text-align: center;">15</td>
		</tr>
		<tr>
			<td style="text-align: center;">16</td>
			<td style="text-align: center;">17</td>
			<td style="text-align: center;">18</td>
			<td style="text-align: center;">19</td>
			<td style="text-align: center;">20</td>
		</tr>
		<tr>
			<td style="text-align: center;">21</td>
			<td style="text-align: center;">22</td>
			<td style="text-align: center;">23</td>
			<td style="text-align: center;">24</td>
			<td style="text-align: center;">25</td>
		</tr>
	</tbody>
</table>

<p> </p>

