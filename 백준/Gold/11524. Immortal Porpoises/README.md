# [Gold II] Immortal Porpoises - 11524 

[문제 링크](https://www.acmicpc.net/problem/11524) 

### 성능 요약

메모리: 30840 KB, 시간: 116 ms

### 분류

분할 정복을 이용한 거듭제곱(exponentiation_by_squaring), 수학(math)

### 문제 설명

<p>As everyone knows, immortal porpoises live on the other side of straight lines and eat live seagulls, although Federal Law prohibits transporting the gulls to them (but that's another story).</p>

<p>The well-known scientist Leo O. Pisa studied immortal porpoises at great length, and made a number of interesting discoveries. He found, for example, that a single pair of porpoises brings forth a pod of 2 babies every year, and that it takes a full year for the babies to mature and start producing pods of their own. Therefore, if you start with one pair of newborn porpoises, at the end of the 1st year, you would still have one pair of porpoises (now mature and ready to procreate). At the end of the second year, you would have a nice new pod of newborns. But you would also have a pair of mature adults! Next year, they would have a second pod of newborns, but their 1st pod would be ready to start producing pods of their own.</p>

<p>Each year, all the porpoises that were around last year are still there. But in addition, all the porpoises who were around two years earlier have babies! However, to prevent the world from being overrun with immortal porpoises, whenever their numbers reach one billion (10<sup>9</sup>) pairs or more, one billion of the pairs mysteriously disappear. Strangely enough, some years the population disappears completely. When that happens, in the next year a single pair miraculously appears. In fact, for any given year, Y, the number of living porpoise pairs is fib(Y) mod 10<sup>9</sup>, where fib(Y) is the Yth value in the well-known Fibonacci sequence.</p>

<p>Suppose each picture <img alt="" src="" style="height:24px; width:22px">represents the number of pairs alive at the end of the year. Then our yearto-year Porpoise Population chart would look something like this:</p>

<table class="table">
	<thead>
		<tr>
			<th>Year</th>
			<th>Pair Count</th>
			<th>Porpoise Pairs Alive</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>1</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>2</td>
			<td>1</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>3</td>
			<td>2</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>4</td>
			<td>3</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>5</td>
			<td>5</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>6</td>
			<td>8</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>7</td>
			<td>13</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>8</td>
			<td>21</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>…</td>
			<td>…</td>
			<td>…</td>
		</tr>
		<tr>
			<td>43</td>
			<td>433494437</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px">…<img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>44</td>
			<td>701408733</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px">…<img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>45</td>
			<td>134903170</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px">…<img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
		<tr>
			<td>46</td>
			<td>836311903</td>
			<td><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px">…<img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"><img alt="" src="" style="height:24px; line-height:20.8px; width:22px"></td>
		</tr>
	</tbody>
</table>

<p>Your job is to write a program that determines the number of immortal porpoise pairs alive at the end of a given number of years, assuming that you start with a newborn pair at the beginning of the 1st year. Since immortal porpoises believe that the universe will exist for exactly 2<sup>48</sup> = 281,474,976,710,656 years, you need not deal with years later than that.</p>

### 입력 

 <p>The first line of input contains a single integer P, (1 ≤ P ≤ 1000), which is the number of data sets that follow. Each data set should be processed identically and independently.</p>

<p>Each data set consists of a single line of input consisting of two space-separated values. The first value is an integer, K, which is the data set number. The next value Y, (1 ≤ Y ≤ 2<sup>48</sup>), is the number of years the porpoises have been alive.</p>

### 출력 

 <p>For each data set there is a single line of output. The line consists of the data set number, K, a single space, and the number of immortal porpoise pairs alive at the end of Y years.</p>

