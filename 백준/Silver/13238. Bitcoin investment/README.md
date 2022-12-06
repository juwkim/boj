# [Silver V] Bitcoin investment - 13238 

[문제 링크](https://www.acmicpc.net/problem/13238) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Bitcoin is a digital asset and a payment system invented by Satoshi Nakamoto.  It is not known whether the name "Satoshi Nakamoto" is real or a pseudonym, or whether the name represents one person or a group of people. It was once rumoured by New Yorker Magazine to be a pseudonym for one of our ex-AIPO finalists, Michael Clear, but he has always strongly denied it. </p>

<p>The value of a bitcoin in euros keeps changes fast. One day a bitcoin may cost 800 euros and two days later go down to 20 euros.</p>

<p>Let’s suppose we know all the future exchange rates of bitcoin to euros and we want to maximize our investment. We don’t have any bitcoin at the beginning. We want to buy one bitcoin and then sell it later. The difference between the buying cost and the selling price will be our benefit (or loss). </p>

<p>Example: these are the cost in euros of a single bitcoin for the next 10 days.</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th>Day</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th>6</th>
			<th>7</th>
			<th>8</th>
			<th>9</th>
			<th>10</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>Price</th>
			<td>5</td>
			<td>11</td>
			<td>4</td>
			<td>2</td>
			<td>8</td>
			<td>10</td>
			<td>7</td>
			<td>4</td>
			<td>3</td>
			<td>6</td>
		</tr>
	</tbody>
</table>

<p>We could buy a bitcoin on day 1 for 5 euros and sell in on day 2 for 11 and we would have a benefit of 6 euros. But, if we instead buy a bitcoin on day 4 (for 2 euros) and sell it on day 6 (for 10 euros) our benefit would be 8 euros. 8 euros is the maximum benefit we can get with these rates.</p>

<p>Your task: given a list of exchange rates. Compute the maximum benefit we can obtain. We can only buy once and sell once. Of course, we must buy before selling. It is possible to buy and sell the same day to get a benefit of 0.</p>

### 입력 

 <p>The first line will contain an integer n representing the number of exchange rates.</p>

<p>The second line will contain n integers from 1 to 10000 representing the exchange rate for the following n days. The number of rates will be at most 100000 (10<sup>5</sup>).</p>

### 출력 

 <p>Write the maximum benefit you could obtain.</p>

