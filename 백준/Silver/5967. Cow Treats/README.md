# [Silver IV] Cow Treats - 5967 

[문제 링크](https://www.acmicpc.net/problem/5967) 

### 성능 요약

메모리: 115004 KB, 시간: 136 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>The cows celebrated another banner month for record milk production and thus have each earned a special treat. They completely fill a W x H rectangle formation (1 <= W <= 25; 1 <= H <= 25) awaiting their treat.</p>

<p>Each cow has a unique figure of merit F_rc (1 <= F_rc <= 1,000,000) which denotes her overall milk production performance. Farmer John thinks it is only fair to prioritize the treats handed out, rewarding the highest producing cows first. He plans to traverse the rectangular formation one row at a time, starting at the beginning of row 1 and giving out all row 1's treats before he starts on row 2 using the same method.</p>

<p>He has asked the cows to reorganize themselves so that the cows with better production are rewarded first. The cows, though, are not so very good at organization. They can either swap a pair of rows or swap a pair of columns of their formation. FJ has asked them to do the best they can by moving the best cow to the upper left corner (row 1, column 1), the next best cow to row 1, column 2 (if possible), and so on. Of course, the cows can not fully sort themselves, but they can do their best by following this heuristic:</p>

<p>determine the order of FJ's treat awards:</p>

<pre>            1    2   3  ...
            W+1 W+2 W+3 ...</pre>

<p>find the highest rated cow; swap rows and columns until she is at row 1, column 1; never move her again</p>

<ul>
	<li>Then execute this rule until as many cows are placed as possible:</li>
	<li>Find the next highest rated cow. Swap rows and columns (without moving any higher-rated cow) to move her to the best possible spot that is still available (e.g., row 1, column 2 if it's available of row 2, column 1 if no slots can be achieved in row 1.</li>
</ul>

<p>By way of example, consider this set of 3 x 4 cows:</p>

<pre>         5  7  4  1
         9 99  2  6
         8  3 10 11</pre>

<p>The cow with 99 is clearly the highest-rated and belows in the upper left corner. Swap rows 1 and 2 then swap columns 1 and 2 (or do it the other way around -- the answer is the same):</p>

<pre>         99  9  2  6
          7  5  4  1
          3  8 10 11</pre>

<p>The cow with 11 should be rewarded as soon as possible after the highest-rated cow. She is current in slot (3,4), the last slot to be rewarded. At this point, it's too late to swap her into the first row or even the first column. Thus, she needs to move to (2,2) by swapping columns 2 and 4 then swapping rows 2 and 3:</p>

<pre>       Swap cols 2 and 4     Swap rows 2 and 3
         99   6  2  9          99   6  2  9
          7   1  4  5    ->     3  11 10  8
          3  11 10  8           7   1  4  5</pre>

<p>The cow with 10 is rewarded directly after the cow with 11. The cow 9 is already rewarded. The cow with 8 is awarded just after the cow with 10. The cow with 7 is rewarded directly after the cow with 8.  The cow with 6 is already rewarded. The cow with 5 would best move to row 3, column 2 but the rows 1 and 2 are frozen as are all the columns.  Thus, cows 1, 4, and 5 do not move, and the second diagram above is the "best the cows can do".</p>

<p>Implement this algorithm for other rectangular arrays of cows.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: W and H</li>
	<li>Lines 2..H+1: Line i+1 contains W space-separated integers F_ic, where c ranges from 1 to W.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..H: Line i contains W space-separated integers representing the i-th row of cows in the cows' final formation.</li>
</ul>

<p> </p>

