# [Silver IV] Cow Solitaire - 6245 

[문제 링크](https://www.acmicpc.net/problem/6245) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 다이나믹 프로그래밍(dp)

### 문제 설명

<p>Late summer on the farm is a slow time, very slow. Betsy has little to do but play cow solitaire. For self-evident reasons, cow solitaire is not so challenging as any number of solitaire games played by humans.</p>

<p>Cow solitaire is played using an N x N (3 <= N <= 7) grid of ordinary playing cards with four suits (Clubs, Diamonds, Hearts, and Spaces) of 13 cards (Ace, 2, 3, 4, ..., 10, Jack, Queen, King). Cards are named with two characters: their value (A, 2, 3, 4, ..., 9, T, J, Q, K) followed by their suit (C, D, H, S). Below is a typical grid when N = 4:</p>

<pre>     8S AD 3C AC     (Eight of Spades, Ace of Diamonds, etc.)
     8C 4H QD QS
     5D 9H KC 7H
     TC QC AS 2D</pre>

<p>To play this solitaire game, Betsy starts in the lower left corner (TC) and proceeds using exactly 2*N-2 moves of 'right' or 'up' to the upper right corner. Along the way, she accumulates points for each card (Ace is worth 1 point, 2 is worth 2 points, ..., 9 is worth 9 points, T is worth 10 points, J is 11, Q is 12, and K is 13) she traverses. Her goal is to amass the highest score.</p>

<p>If Betsy's path was TC-QC-AS-2C-7H-QS-AC, her score would be 10+12+1+2+7+12+1=45. Had she taken the left side then top (TC-5D-8C-8S-AD-3C-AC), her score would be 10+5+8+8+1+3+1=36, not as good as the other route. The best score for this grid is 69 points (TC-QC-9H-KC-QD-QS-AC => 10+12+9+13+12+12+1).</p>

<p>Betsy wants to know the best score she can achieve. One of the geek cows once told her something about "working from the end back to the beginning," but she didn't understand what they meant.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 lists the cards on row i (row 1 is the top row) using N space-separated card names arranged in the obvious order.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single line with an integer that is the best possible score Betsy can achieve.</li>
</ul>

